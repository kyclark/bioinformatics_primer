#!/usr/bin/env python3
"""txt2fa"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Text to FASTA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output dir',
                        metavar='DIR',
                        type=str,
                        default='out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for fnum, fh in enumerate(args.file, start=1):
        basename = os.path.basename(fh.name)
        print('{:3}: {}'.format(fnum, basename))
        out_file = os.path.join(out_dir, basename)
        out_fh = open(out_file, 'wt')
        for i, line in enumerate(fh, start=1):
            out_fh.write('>{}\n{}'.format(i, line))
        out_fh.close()
        num = fnum

    print('Done, processed {} file{}.'.format(fnum, '' if fnum == 1 else 's'))

# --------------------------------------------------
if __name__ == '__main__':
    main()
