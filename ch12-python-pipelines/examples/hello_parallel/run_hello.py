#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-03-28
Purpose: Run "hello.sh" in parallel
"""

import argparse
import os
import tempfile
import sys
import subprocess
from shutil import which


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Simple pipeline using GNU parallel',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'name', metavar='str', nargs='+', help='Names for hello.sh')

    parser.add_argument(
        '-p',
        '--program',
        help='Program to run',
        metavar='str',
        type=str,
        default='./hello.sh')

    parser.add_argument(
        '-P',
        '--parallel',
        help='Program to run',
        metavar='str',
        type=str,
        default=which('parallel'))

    parser.add_argument(
        '-n',
        '--num_procs',
        help='Number of parallel processes',
        metavar='int',
        type=int,
        default=8)

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
def main():
    """Make a jazz noise here"""
    args = get_args()
    prg = args.program

    if not os.path.isfile(prg):
        die('Missing expected program "{}"'.format(prg))

    names = []
    for name in args.name:
        if os.path.isfile(name):
            fh = open(name)
            names.extend(fh.read().splitlines())
        else:
            names.append(name)

    job_file = tempfile.NamedTemporaryFile(delete=False, mode='wt')
    for i, name in enumerate(names):
        job_file.write('{} "{}-{}"\n'.format(prg, i, name))
    job_file.close()

    run_job_file(
        job_file=job_file.name,
        msg='Saying hello!',
        parallel=args.parallel,
        num_procs=args.num_procs)

    print('Done.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
