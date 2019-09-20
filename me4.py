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

    if not sys.argv[1:]:
        raise RuntimeError("Missing name of file to use")

    if not os.path.exists(sys.argv[1]):
        raise RuntimeError("Specified file does not exist: " + sys.argv[1])

    with open(sys.argv[1], 'r') as in_file:
        for line in in_file.readlines():
            print(line.rstrip("\n"))
