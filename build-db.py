#!/usr/bin/env python
"""Build the database from all the CSV files"""
import csv
import os
from typing import List

from data.headers import FIRST_ROW_LOOKUP, SECOND_ROW_LOOKUP
import models


def get_citation_from_year_and_id(year: int, id_: int) -> str:
    """Lookup the citation given the submission year and submission id

    Args:
        year: the year the paper was submitted
        id_: an excerpt of which paper to grab from the REDW lookup
            example: '4, pp. 19-25', we would want the '4'
    """
    paper_id = int(id_.split(',')[0])
    """
    TODO BRADY: split up cumulative-index into per year sections
    Can filter on "[Year] Workshop Record"
    Should be easy to get the data at that point
    """


def strip_bad_see_characters(results_str: str) -> str:
    """Strip bad characters from the results cell.

    Don't use square root symbols for checkboxes please. Use an 'x'...
    """
    output_str = ''
    for char in ['H', 'P', 'L', 'N']:
        if char in results_str:
            output_str += char
    return output_str


def parse_and_add_result(curr_row: List[str], last_valid_row: List[str],
                         part: models.Part, year: int):
    """Create a Results from the CSV data

    The dataset is not "fully filled out" here and only fills out the
    paper number and author for the first row if it applies to many
    rows, so we have to keep track of the last fully filled out row.
    Sometimes the rows will be the same and that's fine.

    PS if you think this function is silly/inefficient, I have a big old data
    set that needs cleaning...

    Args:
        curr_row: the row to grab all the test specific info
        last_valid_row: the row to grab all the citation info
        part: which Part to add the Result to
        year: which year the paper was published in
            Required in order to to find the citation
    """
    kwargs = {}

    # Common Parsing
    kwargs['part'] = part
    if curr_row[SECOND_ROW_LOOKUP['Terrestrial']]:
        kwargs['data_type'] = 'Terrestrial'
    else:
        kwargs['data_type'] = 'Flight'
    kwargs['citation'] = get_citation_from_year_and_id(year, last_valid_row[0])

    # TID Parsing
    if curr_row[SECOND_ROW_LOOKUP['Co60']]:
        kwargs['tid_hdr'] = True
    if curr_row[SECOND_ROW_LOOKUP['ELDRS']]:
        kwargs['tid_ldr'] = True
    if curr_row[SECOND_ROW_LOOKUP['Protons']]:
        kwargs['tid_proton'] = True
    if curr_row[SECOND_ROW_LOOKUP['Electrons']]:
        kwargs['tid_electron'] = True

    # SEE Parsing
    SEE_TYPES = ['SEU', 'SET', 'SEFI', 'SEL', 'SEB', 'SEGR']
    for see_type in SEE_TYPES:
        val = curr_row[SECOND_ROW_LOOKUP[see_type]]
        if val == '':
            continue
        elif see_type == 'SEU':
            kwargs['see_upset'] = strip_bad_see_characters(val)
        elif see_type == 'SET':
            kwargs['see_transient'] = strip_bad_see_characters(val)
        elif see_type == 'SEFI':
            kwargs['see_fault'] = strip_bad_see_characters(val)
        elif see_type == 'SEL':
            kwargs['see_latchup'] = strip_bad_see_characters(val)
        elif see_type == 'SEB':
            kwargs['see_burnout'] = strip_bad_see_characters(val)
        elif see_type == 'SEGR':
            kwargs['see_gate_rupture'] = strip_bad_see_characters(val)
        else:
            raise ValueError("Invalid SEE type")

    # Displacement Damage Parsing
    # Yes I just realized I had a key conflict. Sue me.
    if curr_row[SECOND_ROW_LOOKUP['Neutrons'] - 1]:
        kwargs['dd_protons'] = True
    if curr_row[SECOND_ROW_LOOKUP['Neutrons']]:
        kwargs['dd_neutrons'] = True

    models.Part.create(**kwargs)


def parse_and_add_part(curr_row: List[str]) -> models.Part:
    """Create a Part from the CSV data"""
    part = models.Part.create(
        name=curr_row[FIRST_ROW_LOOKUP['Part No.']],
        device_type=curr_row[FIRST_ROW_LOOKUP['Type']],
        manufacturer=curr_row[FIRST_ROW_LOOKUP['Manufacture']])
    return part


def main():
    for fname in [
            'data/hiemstra2007-page-2-table-1.csv',
            'data/hiemstra2007-page-3-table-1.csv',
            'data/hiemstra2007-page-4-table-1.csv'
    ]:
        if not fname.endswith('.csv'):
            continue

        print(f'==== ADDING {fname} ====')
        with open(fname, 'r') as f:
            # This line sucks and is hardcoded, but I'm lazy
            year = int(os.path.split(fname)[1][8:12])

            reader = csv.reader(f, delimiter=',')
            # Skip header rows
            next(reader)
            next(reader)

            last_valid_row = []
            for row in reader:
                if row[FIRST_ROW_LOOKUP['First Author']] != '':
                    last_valid_row = row

                part = parse_and_add_part(row)

                parse_and_add_result(row, last_valid_row, part, year)


if __name__ == "__main__":
    models.db.connect()
    main()
    models.db.close()
