#!/usr/bin/env python3
"""Find paired reads"""

import argparse
import os
import re
import sys
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run KrakenUniq',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-q',
                        '--query',
                        metavar='str',
                        help='Input file/directory',
                        nargs='+',
                        required=True)

    args = parser.parse_args()

    for q in args.query:
        if not any([os.path.isdir(q), os.path.isfile(q)]):
            parser.error('--query "{}" neither file nor directory'.format(q))

    return args


# --------------------------------------------------
def unique_extensions(files):
    exts = set()
    for file in files:
        _, ext = os.path.splitext(file)
        exts.add(ext[1:])  # skip leading "."

    return exts


# --------------------------------------------------
def find_input_files(query):
    """Find input files from list of files/dirs"""

    files = []
    for qry in query:
        if os.path.isdir(qry):
            for filename in os.scandir(qry):
                if filename.is_file():
                    files.append(filename.path)
        elif os.path.isfile(qry):
            files.append(qry)
        else:
            raise Exception(
                'query "{}" neither file nor directory'.format(qry))

    extensions = unique_extensions(files)
    paired_re = re.compile('(.+)[_-][Rr]?[12](?:_\d+)?\.(?:' +
                           '|'.join(extensions) + ')$')

    unpaired = []
    paired = defaultdict(list)
    for fname in files:
        basename = os.path.basename(fname)
        paired_match = paired_re.search(basename)

        if paired_match:
            sample_name = paired_match.group(1)
            paired[sample_name].append(fname)
        else:
            unpaired.append(fname)

    return paired, unpaired


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    paired, unpaired = find_input_files(args.query)

    print(paired)
    print(unpaired)

# --------------------------------------------------
if __name__ == '__main__':
    main()
