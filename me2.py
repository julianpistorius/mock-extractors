"""
Mock Extractor 2

Input: A set of files
Output: Produce a single CSV file with columns: filename, timestamp
"""

import sys

if __name__ == '__main__':
    print('Arguments:', len(sys.argv))
    print('List:', str(sys.argv))
