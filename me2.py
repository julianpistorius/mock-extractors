#!/usr/bin/env python3

"""
Mock Extractor 2

Input: A set of files
Output: Produce a single CSV file with columns: filename, timestamp
"""

import os
import sys
from datetime import datetime

if __name__ == '__main__':
    print('Arguments:', len(sys.argv))
    print('List:', str(sys.argv))

    input_dir = sys.argv[1]
    print(f'Looking at folder {input_dir} for input files')
    output_dir = sys.argv[2]
    print(f'Output directory: {output_dir}')

    # Scan for .dmy files
    num_found = 0
    out_filename = 'testing.csv'
    out_filename = output_dir.rstrip('/') + '/' + out_filename
    print(f'out_filename: {out_filename}')
    with open(out_filename, 'w') as out_file:
        for item in os.listdir(input_dir):
            path_and_filename = input_dir.rstrip('/') + '/' + item
            is_a_file = os.path.isfile(path_and_filename)
            has_correct_extension = item.endswith('.dmy')
            print(
                f'item: {item}    is_a_file: {is_a_file}  has_correct_extension: {has_correct_extension}')
            if is_a_file and has_correct_extension:
                num_found += 1
                out_file.write(item + ", " + str(datetime.now()) + '\n')

    print("Found " + str(num_found) + " files")
