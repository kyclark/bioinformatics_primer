#!/usr/bin/env python3

import argparse
import logging
import os
import random
import sys
import time


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Demonstrate logging',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-d', '--debug', help='Debug mode', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    prg = sys.argv[0]
    prg_name, _ = os.path.splitext(os.path.basename(prg))

    logging.basicConfig(
        filename=prg_name + '.log',
        filemode='a',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    logging.debug('Starting')
    for i in range(1, 11):
        method = random.choice([
            logging.info, logging.warning, logging.error, logging.critical,
            logging.debug
        ])
        method('{}: Hey!'.format(i))
        time.sleep(1)

    logging.debug('Done')

    print('Done.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
