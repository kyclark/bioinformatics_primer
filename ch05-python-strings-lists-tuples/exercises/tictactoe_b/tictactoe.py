#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-02-06
Purpose: Tic-Tac-Toe board
"""

import argparse
import re
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--state',
        help='Board state',
        metavar='str',
        type=str,
        default='.........')

    parser.add_argument(
        '-p', '--player', help='Player', metavar='str', type=str, default=None)

    parser.add_argument(
        '-c',
        '--cell',
        help='Cell to apply -p',
        metavar='int',
        type=int,
        default=None)

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
    state = args.state
    player = args.player
    cell = args.cell

    if player and player not in 'XO':
        die('Invalid player "{}", must be X or O'.format(player))

    if cell is not None and not 1 <= cell <= 9:
        die('Invalid cell "{}", must be 1-9'.format(cell))

    if any([player, cell]) and not all([player, cell]):
        die('Must provide both --player and --cell')

    if not re.search('^[.XO]{9}$', state):
        die('Invalid state "{}", must be 9 characters of only -, X, O'.format(
            state))

    bar = '-------------'
    cells_tmpl = '| {} | {} | {} |'

    cells = []
    for i, char in enumerate(state, start=1):
        cells.append(str(i) if char == '.' else char)

    if player and cell:
        if cells[cell - 1] not in 'XO':
            cells[cell - 1] = player
        else:
            die('Cell {} already taken'.format(cell))

    print('\n'.join([
        bar,
        cells_tmpl.format(cells[0], cells[1], cells[2]), bar,
        cells_tmpl.format(cells[3], cells[4], cells[5]), bar,
        cells_tmpl.format(cells[6], cells[7], cells[8]), bar
    ]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
