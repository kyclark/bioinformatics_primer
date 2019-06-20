#!/usr/bin/env python3
"""BAM to FASTx"""

import argparse
import os
from parallelprocs import run
from dire import warn


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='BAM to FASTx',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        help='Input BAM files')

    parser.add_argument('-f',
                        '--format',
                        help='Output format',
                        metavar='str',
                        type=str,
                        choices=['fasta', 'fastq'],
                        default='fasta')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-p',
                        '--procs',
                        help='Num procs',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-v', '--verbose', help='Verbose', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fmt = args.format
    out_dir = args.outdir or out_fmt
    out_ext = '.fa' if out_fmt == 'fasta' else '.fq'

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    commands = []
    for i, file in enumerate(args.file, start=1):
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(file))
            continue

        basename = os.path.basename(file)
        root, _ = os.path.splitext(basename)
        out_path = os.path.join(out_dir, root + out_ext)
        print('{:3}: {}'.format(i, basename))
        commands.append('samtools {} "{}" > {}'.format(out_fmt, file,
                                                       out_path))
    try:
        run(commands, halt=1, num_procs=args.procs, verbose=args.verbose)
    except Exception as e:
        print(e)

    print('Done, see output in "{}"'.format(out_dir))


# --------------------------------------------------
if __name__ == '__main__':
    main()
