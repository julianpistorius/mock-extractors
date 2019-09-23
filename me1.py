#!/usr/bin/env python3

"""
Mock Extractor 1

Input: A string indicating the unique name of the workflow run (optional)
Output: Creates an empty numbered file (timestamp based) incorporating the
input string
"""
import sys
from datetime import datetime
import random

if __name__ == '__main__':
    print('Arguments:', len(sys.argv))
    print('List:', str(sys.argv))

    out_name = str(datetime.now()).replace(' ', '_').replace(':', '-').replace(
        '.', '_')
    out_name += '.dmy'

    if sys.argv[1:]:
        out_name = sys.argv[1].rstrip('/') + '/' + out_name
        print(f'out_name: {out_name}')

    random_value = str(random.randint(1000, 10000))
    with open(out_name, 'w') as out_file:
        out_file.write(','.join(sys.argv[1:] + [random_value]) + '\n')
