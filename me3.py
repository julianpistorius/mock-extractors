"""
Mock Extractor 3

Input: A CSV file with columns: filename, timestamp
Output: A set of sequentially numbered files with timestamp info as content
"""

import os
import sys

if __name__ == '__main__':
    print('Arguments:', len(sys.argv))
    print('List:', str(sys.argv))

    csv_filename = sys.argv[1] if len(sys.argv) > 1 else 'testing.csv'
    if not os.path.exists(csv_filename):
        raise RuntimeError("Unable to find csv file: " + csv_filename)

    num_rows = 0
    with open(csv_filename, "r") as in_file:
        for one_row in in_file.readlines():
            num_rows += 1
            with open(str(num_rows) + '.txt', 'w') as out_file:
                out_file.write(one_row)

    print("Found " + str(num_rows) + " rows in file " + csv_filename)
