#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-02-22
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
from xml.etree.ElementTree import ElementTree


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('xml', metavar='XML', help='XML input', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='str',
        type=str,
        default='out')

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
    xml_files = args.xml
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for file in xml_files:
        print('>>>>>>', file)
        tree = ElementTree()
        root = tree.parse(file)

        d = []
        for key, value in root.attrib.items():
            d.append(('sample.' + key, value))

        for id_ in root.find('IDENTIFIERS'):
            d.append(('id.' + id_.tag, id_.text))

        for attr in root.findall('SAMPLE_ATTRIBUTES/SAMPLE_ATTRIBUTE'):
            d.append(('attr.' + attr.find('TAG').text, attr.find('VALUE').text))

        for key, value in d:
            print('{:25}: {}'.format(key, value))

        print()

# --------------------------------------------------
if __name__ == '__main__':
    main()
