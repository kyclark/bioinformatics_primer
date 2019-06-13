#!/usr/bin/env python3
"""
Author:  Ken Youens-Clark <kyclark@gmail.com>
Purpose: Convert a delimited text file to JSON
"""

import argparse
import csv
import json
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'tabfile', metavar='str', nargs='+', help='A positional argument')

    parser.add_argument(
        '-s',
        '--sep',
        help='Field separator',
        metavar='str',
        type=str,
        default='\t')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output dir',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-i',
        '--indent',
        help='Indent level',
        metavar='int',
        type=int,
        default=2)

    parser.add_argument(
        '-n',
        '--normalize_headers',
        help='Normalize headers',
        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    indent_level = args.indent
    out_dir = args.outdir
    fs = args.sep
    norm_hdr = args.normalize_headers
    tabfiles = args.tabfile

    if len(tabfiles) < 1:
        print('No input files')
        sys.exit(1)

    if indent_level < 0:
        indent_level = 0

    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for i, tabfile in enumerate(tabfiles, start=1):
        basename = os.path.basename(tabfile)
        filename, _ = os.path.splitext(basename)
        dirname = os.path.dirname(os.path.abspath(tabfile))
        print('{:3}: {}'.format(i, basename))
        write_dir = out_dir if out_dir else dirname
        out_path = os.path.join(write_dir, filename + '.json')
        out_fh = open(out_path, 'wt')

        with open(tabfile) as fh:
            reader = csv.DictReader(fh, delimiter=fs)
            if norm_hdr:
                reader.fieldnames = list(map(normalize, reader.fieldnames))
            out_fh.write(json.dumps(list(reader), indent=indent_level))


# --------------------------------------------------
def normalize(hdr):
    return re.sub(r'[^A-Za-z0-9_]', '', hdr.lower().replace(' ', '_'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
