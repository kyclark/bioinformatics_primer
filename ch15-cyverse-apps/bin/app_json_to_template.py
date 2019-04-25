#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-01-30
Purpose: Create template.sh from app.json
"""

import argparse
import json
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Create template.sh from app.json',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-j',
        '--app_json',
        help='The app.json file',
        metavar='str',
        type=str,
        default='app.json')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file name',
        metavar='str',
        type=str,
        default='template.sh')

    parser.add_argument(
        '-f',
        '--force',
        help='Force overwrite of outfile',
        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    app_json = args.app_json
    out_file = args.outfile
    force = args.force

    if not os.path.isfile(app_json):
        die('--app_json "{}" is not a file'.format(app_json))

    if os.path.isfile(out_file) and not force:
        die('Will not overwrite --outfile "{}" without --force'.format(
            out_file))

    out_fh = open(out_file, 'w')
    with open(app_json) as fh:
        data = json.loads(fh.read())
        template = '#!/usr/bin/env bash\n\nsh run.sh {}\n'
        args = []

        for key in ['inputs', 'parameters']:
            if key in data:
                for val in data[key]:
                    args.append('${' + val['id'] + '}')

        out_fh.write(template.format(' '.join(args)))

    print('Done, see outfile "{}"'.format(out_file))


# --------------------------------------------------
if __name__ == '__main__':
    main()
