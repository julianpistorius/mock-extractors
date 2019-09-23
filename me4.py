#!/usr/bin/env python3

"""
Mock Extractor 4

Input: A set of sequentially numbered files with timestamp info as content
Output: A report with summary data about the set of input files (e.g. number of
files and min/max timestamp)
"""

import os
import sys

if __name__ == '__main__':
    print('Arguments:', len(sys.argv))
    print('List:', str(sys.argv))

    input_dir = sys.argv[1].rstrip('/')
    print(f'Looking at folder {input_dir} for input files')
    output_dir = sys.argv[2].rstrip('/')
    print(f'Output directory: {output_dir}')

    if not os.path.exists(input_dir):
        raise RuntimeError(f'Input directory not found: {input_dir}')
    if not os.path.isdir(input_dir):
        raise RuntimeError(f'Input directory is not a directory: {input_dir}')
    if not os.path.exists(output_dir):
        raise RuntimeError(f'Output directory not found: {output_dir}')
    if not os.path.isdir(output_dir):
        raise RuntimeError(f'Output directory is not a directory: {output_dir}')

    out_filename = output_dir + '/' + 'report.csv'

    num_found = 0
    min_timestamp = None
    max_timestamp = None

    for item in os.listdir(input_dir):
        path_and_filename = input_dir.rstrip('/') + '/' + item
        is_a_file = os.path.isfile(path_and_filename)
        has_correct_extension = item.endswith('.txt')
        print(
            f'item: {item}    is_a_file: {is_a_file}  has_correct_extension: {has_correct_extension}')
        if is_a_file and has_correct_extension:
            num_found += 1
            with open(path_and_filename, 'r') as input_file:
                line = input_file.readline()
                dmy_file, timestamp = line.split(',')
                timestamp = timestamp.strip()
                if not min_timestamp or timestamp < min_timestamp:
                    min_timestamp = timestamp
                if not max_timestamp or timestamp > max_timestamp:
                    max_timestamp = timestamp

    with open(out_filename, 'w') as out_file:
        out_file.write(
            ','.join(map(str, [num_found, min_timestamp, max_timestamp])))
