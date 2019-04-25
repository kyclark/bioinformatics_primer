#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-02-25
Purpose: Demonstrate GNU Parallel
"""

import argparse
import os
import sys
import subprocess
import tempfile as tmp


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Demonstrate GNU Parallel',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-f',
        '--file',
        metavar='FILE',
        help='A positional argument',
        default='/usr/share/dict/words')

    parser.add_argument(
        '-c',
        '--cores',
        help='Number of cores',
        metavar='INT',
        type=int,
        default=4)

    parser.add_argument(
        '-m',
        '--max_lines',
        help='Maximum number of input lines',
        metavar='INT',
        type=int,
        default=25)

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
    in_file = args.file
    max_lines = args.max_lines
    num_cores = args.cores

    if not os.path.isfile(in_file):
        die('"{}" is not a file'.format(in_file))

    jobfile = tmp.NamedTemporaryFile(delete=False, mode='wt')
    for i, line in enumerate(open(in_file), start=1):
        jobfile.write('echo "{} {}"\n'.format(i, line.rstrip()))
        if i == max_lines: break

    jobfile.close()

    print('Starting parallel on {} cores'.format(num_cores))
    cmd = 'parallel -j {} --halt soon,fail=1 < {}'.format(
        num_cores, jobfile.name)

    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        die('Error:\n{}\n{}\n'.format(err.stderr, err.stdout))
    finally:
        os.remove(jobfile.name)

    print('Finished parallel')


# --------------------------------------------------
if __name__ == '__main__':
    main()
