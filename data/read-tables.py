#!/usr/bin/env python3
"""Read tables from a PDF and write them to a CSV"""
import os

import camelot


def main():
    for fname in os.listdir():
        if not (fname.startswith('hiem') and fname.endswith('.pdf')):
            print(f'Invalid PDF {fname}, skipping')
            continue
        print(f'Parsing {fname}')
        tables = camelot.read_pdf(fname, pages='2-end')
        csv_fname = os.path.splitext(fname)[0] + '.csv'
        tables.export(csv_fname, f='csv')


if __name__ == "__main__":
    main()
