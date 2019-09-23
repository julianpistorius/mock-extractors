#!/usr/bin/env python3

"""
Mock Extractor 3

Input: A CSV file with columns: filename, timestamp
Output: A set of sequentially numbered files with timestamp info as content
"""

import os
import sys

if __name__ == '__main__':
    print('Arguments:', len(sys.argv))
    print('List:', str(sys.argv))

    csv_filename = sys.argv[1]
    print(f'input_file: {csv_filename}')
    output_dir = sys.argv[2].rstrip('/')
    print(f'Output directory: {output_dir}')
    if not os.path.exists(csv_filename):
        raise RuntimeError(f'Unable to find csv file: {csv_filename}')
    if not os.path.exists(output_dir):
        raise RuntimeError(f'Output directory not found: {output_dir}')
    if not os.path.isdir(output_dir):
        raise RuntimeError(f'Output directory is not a directory: {output_dir}')

    with open(csv_filename, "r") as in_file:
        for row_index, one_row in enumerate(in_file.readlines()):
            out_filename = str(row_index) + '.txt'
            out_filename = output_dir + '/' + out_filename
            with open(out_filename, 'w') as out_file:
                out_file.write(one_row)
    print("Found " + str(row_index + 1) + " rows in file " + csv_filename)
