#!/usr/bin/env python3
"""Validate headers on all the CSV files.

The Excel sheet used to make this data format is truly bizarre, so I having a
file like this really helps to make sure all the data is correct.
"""
import csv
import os

import headers


def check_row(data_row, truth_row):
    """Checks to see if the data row matches the truth row"""
    for data, truth in zip(data_row, truth_row):
        data.strip()
        truth.strip()
        if data != truth:
            output_str = "Error: "
            output_str += f'"{data}", "{truth}"'
            print(output_str)


def main():
    for fname in os.listdir():
        if not (fname.startswith('hiemstra2008') and fname.endswith('.csv')):
            continue

        print(f'==== CHECKING {fname} ====')
        with open(fname, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for idx, row in enumerate(reader):
                if idx == 0:
                    first_row = row
                elif idx == 1:
                    second_row = row
                else:
                    break
                # print(row)

        check_row(first_row, headers.GOLDEN_FIRST_ROW)
        check_row(second_row, headers.GOLDEN_SECOND_ROW)


if __name__ == "__main__":
    main()
