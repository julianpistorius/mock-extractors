"""
Mock Extractor 1

Input: A string indicating the unique name of the workflow run
Output: Creates an empty numbered file (timestamp based) incorporating the
input string
"""
import sys

if __name__ == '__main__':
    print('Arguments:', len(sys.argv))
    print('List:', str(sys.argv))
