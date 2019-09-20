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

    cur_dir = None
    if not sys.argv[1:]:
        print("Using current folder to look for files: " + os.getcwd())
    else:
        print("Looking at folder " + sys.argv[1] + " for files")
        cur_dir = os.getcwd()
        os.chdir(sys.argv[1])

    # Scan for .dmy files
    num_found = 0
    with open('testing.csv', 'w') as out_file:
        for item in os.listdir('.'):
            if os.path.isfile(item) and item.endswith('.dmy'):
                num_found += 1
                out_file.write(item + ", " + str(datetime.now()) + '\n')

    # Change back to original folder
    if cur_dir:
        os.chdir(cur_dir)

    print ("Found " + str(num_found) + " files")
