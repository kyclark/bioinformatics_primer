#!/usr/bin/env python3
"""BAM to FASTx"""

import argparse
import os
import sys
import tempfile
import subprocess
from dire import warn
from shutil import which


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
                        default='bam2fx-out')

    parser.add_argument('-P',
                        '--parallel',
                        help='Program to run',
                        metavar='str',
                        type=str,
                        default=which('parallel'))

    parser.add_argument('-n',
                        '--num_procs',
                        help='Number of parallel processes',
                        metavar='int',
                        type=int,
                        default=8)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir
    out_fmt = args.format
    out_ext = '.fa' if out_fmt == 'fasta' else '.fq'

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    job_file = tempfile.NamedTemporaryFile(delete=False, mode='wt')
    for i, file in enumerate(args.file):
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(file))
            continue

        basename, _ = os.path.splitext(os.path.basename(file))
        out_path = os.path.join(out_dir, basename + out_ext)
        job_file.write('samtools {} "{}" > {}\n'.format(
            out_fmt, file, out_path))
    job_file.close()

    run_job_file(job_file=job_file.name,
                 msg='samtools ' + out_fmt,
                 parallel=args.parallel,
                 num_procs=args.num_procs)

    print('Done.')

# --------------------------------------------------
def line_count(fname):
    """Count the number of lines in a file"""

    n = 0
    for _ in open(fname):
        n += 1

    return n


# --------------------------------------------------
def run_job_file(job_file, msg='Running job', parallel='', num_procs=1):
    """Run a job file if there are jobs"""

    num_jobs = line_count(job_file)
    warn('{} (# jobs = {})'.format(msg, num_jobs))

    if num_jobs > 0:
        if os.path.isfile(parallel):
            cmd = 'parallel --halt soon,fail=1 -P {} < {}'.format(
                num_procs, job_file)

            try:
                subprocess.run(cmd, shell=True, check=True)
            except subprocess.CalledProcessError as err:
                die('Error:\n{}\n{}\n'.format(err.stderr, err.stdout))
            finally:
                os.remove(job_file)
        else:
            try:
                for cmd in open(job_file):
                    rv, out = subprocess.getstatusoutput(cmd)
                    if rv != 0:
                        warn('Failed to run: {}\nError: {}'.format(cmd, out))
                    else:
                        print('Success: "{}"'.format(out))
            finally:
                os.remove(job_file)

    return True


# --------------------------------------------------
if __name__ == '__main__':
    main()
