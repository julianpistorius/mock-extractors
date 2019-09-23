#!/usr/bin/env python3

"""
Mock Extractor 5

To test recovering from errors this extractor randomly fails.

Input: A sequentially numbered file
Output: The same file, renamed
"""

import os
import random
import sys
from shutil import copyfile
import time

if __name__ == '__main__':
    print('Arguments:', len(sys.argv))
    print('List:', str(sys.argv))

    sleep_length = random.triangular(0.1, 2.0)

    print(f'Sleeping for {sleep_length} seconds...')
    time.sleep(sleep_length)

    failure_rate = 0.25
    print(f'failure_rate: {failure_rate}')
    russian_roulette = random.random()
    if russian_roulette > failure_rate:
        print(f'Phew! {russian_roulette}')
    else:
        raise RuntimeError(f'Oops! {russian_roulette}')

    input_file = sys.argv[1]
    print(f'input_file: {input_file}')
    output_dir = sys.argv[2].rstrip('/')
    print(f'Output directory: {output_dir}')

    if not os.path.exists(input_file):
        raise RuntimeError(f'Input file not found: {input_file}')
    if not os.path.isfile(input_file):
        raise RuntimeError(f'Input file is not a file: {input_file}')
    if not input_file.endswith('.txt'):
        raise RuntimeError(
            f'Input file does not have the right extension: {input_file}')
    if not os.path.exists(output_dir):
        raise RuntimeError(f'Output directory not found: {output_dir}')
    if not os.path.isdir(output_dir):
        raise RuntimeError(f'Output directory is not a directory: {output_dir}')

    out_filename = output_dir + '/' + os.path.basename(input_file) + '.copy'

    copyfile(input_file, out_filename)
