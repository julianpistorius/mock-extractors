"""
Mock Extractor 1

Input: A string indicating the unique name of the workflow run (optional)
Output: Creates an empty numbered file (timestamp based) incorporating the
input string
"""
import sys
from datetime import datetime

if __name__ == '__main__':
    print('Arguments:', len(sys.argv))
    print('List:', str(sys.argv))
    out_name = str(datetime.now()).replace(' ', '_').replace(':', '-').replace('.', '_')
    out_name += '.dmy'
    with open(out_name, 'w') as out_file:
        out_file.write(','.join(sys.argv[1:]) + '\n')
