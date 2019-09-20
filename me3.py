"""
Mock Extractor 3

Input: A CSV file with columns: filename, timestamp
Output: A set of sequentially numbered files with timestamp info as content
"""

import sys

if __name__ == '__main__':
    print('Arguments:', len(sys.argv))
    print('List:', str(sys.argv))
