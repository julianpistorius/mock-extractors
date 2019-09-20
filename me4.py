"""
Mock Extractor 4

Input: A set of sequentially numbered files with timestamp info as content
Output: A report with summary data about the set of input files (e.g. number of
files and min/max timestamp)
"""

import sys

if __name__ == '__main__':
    print('Arguments:', len(sys.argv))
    print('List:', str(sys.argv))
