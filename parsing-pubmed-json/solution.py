#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-16
Purpose: Fetch PubMed info, cf. http://www.ncbi.nlm.nih.gov/books/NBK25499/
"""

import argparse
import json
import pprint
import requests
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Fetch PubMed info',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pubmed_id',
                        metavar='int',
                        type=int,
                        nargs='+',
                        help='PubMed ID(s)')

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

    pubmed_url = ('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
                  'esummary.fcgi?db=pubmed&retmode=json&id={}')

    for pubmed_id in args.pubmed_id:
        r = requests.get(pubmed_url.format(pubmed_id))
        if r.status_code == 200:
            data = json.loads(r.text)
            result = data.get('result')
            if result:
                info = result.get(str(pubmed_id))
                if info:
                    pprint.PrettyPrinter().pprint(info)
                    print(info['title'], info['lastauthor'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
