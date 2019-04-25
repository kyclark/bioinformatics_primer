#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-02-20
Purpose: Run cd-hit, find unclustered proteins
"""

import argparse
import datetime
import logging
import os
import re
import signal
import sys
from subprocess import getstatusoutput
from shutil import which
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Run cd-hit, find unclustered proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        required=True)

    parser.add_argument(
        '-c',
        '--seq_id_threshold',
        help='cd-hit Sequence identity threshold',
        metavar='float',
        type=float,
        default=0.9)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')

    parser.add_argument(
        '-l',
        '--logfile',
        help='Log file',
        metavar='str',
        type=str,
        default='.log')

    parser.add_argument('-d', '--debug', help='Debug', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def die(msg='Something bad happened'):
    """log a critical message() and exit with error"""
    logging.critical(msg)
    sys.exit(1)


# --------------------------------------------------
def run_cdhit(proteins_file, seq_id_threshold):
    """Run cd-hit"""
    cdhit = which('cd-hit')

    if not cdhit:
        die('Cannot find "cd-hit"')

    out_file = os.path.basename(proteins_file) + '.cdhit'
    out_path = os.path.join(os.path.dirname(proteins_file), out_file)

    logging.debug('Found cd-hit "{}"'.format(cdhit))
    cmd = '{} -c {} -i {} -o {}'.format(cdhit, seq_id_threshold,
                                        proteins_file, out_path)
    logging.debug('Running "{}"'.format(cmd))
    rv, out = getstatusoutput(cmd)

    if rv != 0:
        die('Non-zero ({}) return from "{}"\n{}\n'.format(rv, cmd, out))

    if not os.path.isfile(out_path):
        die('Failed to create "{}"'.format(out_path))

    logging.debug('Finished cd-hit, found cluster file "{}"'.format(out_path))

    return out_file


# --------------------------------------------------
def get_unclustered(cluster_file, proteins_file, out_file):
    """Find the unclustered proteins in the cd-hit output"""

    if not os.path.isfile(cluster_file):
        die('cdhit "{}" is not a file'.format(cluster_file))

    logging.debug('Parsing "{}"'.format(cluster_file))

    clustered = set([rec.id for rec in SeqIO.parse(cluster_file, 'fasta')])

    # Alternate (longer) way:
    # clustered = set()
    # for rec in SeqIO.parse(cluster_file, 'fasta'):
    #     clustered.add(rec.id)

    logging.debug('Will write to "{}"'.format(out_file))
    out_fh = open(out_file, 'wt')
    num_total = 0
    num_unclustered = 0

    for rec in SeqIO.parse(proteins_file, 'fasta'):
        num_total += 1
        prot_id = re.sub(r'\|.*', '', rec.id)
        if not prot_id in clustered:
            num_unclustered += 1
            SeqIO.write(rec, out_fh, 'fasta')

    logging.debug(
        'Finished writing unclustered proteins'.format(num_unclustered))

    return (num_unclustered, num_total)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    proteins_file = args.proteins
    out_file = args.outfile
    log_file = args.logfile

    if not os.path.isfile(proteins_file):
        die('--proteins "{}" is not a file'.format(arg_name, proteins_file))

    logging.basicConfig(
        filename=log_file,
        filemode='a',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    def sigint(sig, frame):
        logging.critical('INT: Exiting early!')
        sys.exit(0)

    signal.signal(signal.SIGINT, sigint)

    banner = '#' * 50
    logging.debug(banner)
    logging.debug('BEGAN {}'.format(str(datetime.datetime.today())))

    cluster_file = run_cdhit(proteins_file, args.seq_id_threshold)
    num_unclustered, num_total = get_unclustered(cluster_file, proteins_file,
                                                 out_file)

    msg = 'Wrote {:,d} of {:,d} unclustered proteins to "{}"'.format(
        num_unclustered, num_total, out_file)

    print(msg)
    logging.debug(msg)
    logging.debug('FINISHED {}'.format(str(datetime.datetime.today())))
    logging.debug(banner)


# --------------------------------------------------
if __name__ == '__main__':
    main()
