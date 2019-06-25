#!/usr/bin/env python3
"""Generic bubble plot"""

import argparse
import csv
import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import sys
from dire import die


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Plot Centrifuge out',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=str,
                        help='Data',
                        nargs='+')

    parser.add_argument('-S',
                        '--sep',
                        help='Field separator',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-x',
                        '--x_axis',
                        help='Column for x-axis',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-y',
                        '--y_axis',
                        help='Column for y-axis',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-s',
                        '--s_axis',
                        help='Column for s-axis',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-X',
                        '--x_label',
                        help='Label for x-axis',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-Y',
                        '--y_label',
                        help='Label for y-axis',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('--x_exclude',
                        help='Exclude values from x',
                        metavar='str',
                        type=str,
                        nargs='*')

    parser.add_argument('--y_exclude',
                        help='Exclude values from y',
                        metavar='str',
                        type=str,
                        nargs='*')

    parser.add_argument('-t',
                        '--title',
                        help='Image title',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-m',
                        '--multiplier',
                        help='Multiplier',
                        metavar='float',
                        type=float,
                        default=1.)

    parser.add_argument('-w',
                        '--image_width',
                        help='Image width',
                        metavar='float',
                        type=float,
                        default=0.)

    parser.add_argument('-H',
                        '--image_height',
                        help='Image height',
                        metavar='float',
                        type=float,
                        default=0.)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-f',
                        '--format',
                        help='Ouput format',
                        metavar='str',
                        type=str,
                        choices=['png', 'pdf'],
                        default='pdf')

    parser.add_argument('-r',
                        '--sort',
                        help='Sort data by x/y',
                        action='store_true')

    parser.add_argument('-l',
                        '--list_cols',
                        help='Show column list and quit',
                        action='store_true')

    parser.add_argument('-O',
                        '--open_image',
                        help='Open the image when done',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for file in args.file:
        basename = os.path.basename(file)
        x_axis = args.x_axis
        y_axis = args.y_axis
        s_axis = args.s_axis
        title = args.title or basename
        sep = args.sep

        if not sep:
            _, ext = os.path.splitext(basename)
            sep = ',' if ext == '.csv' else '\t'

        df = pd.read_csv(file, sep=sep)
        col_names = df.columns
        nrows, ncols = df.shape

        if args.list_cols:
            print('Columns in "{}"\n{}\n'.format(
                basename, '\n'.join(
                    map(lambda t: '{:3}: {}'.format(*t),
                        enumerate(col_names, 1)))))
            sys.exit(0)

        if x_axis and x_axis.isdigit() and not x_axis in col_names:
            x_axis = col_names[int(x_axis) - 1]

        if y_axis and y_axis.isdigit() and not y_axis in col_names:
            y_axis = col_names[int(y_axis) - 1]

        if s_axis and s_axis.isdigit() and not s_axis in col_names:
            s_axis = col_names[int(s_axis) - 1]

        if not x_axis and ncols >= 1:
            x_axis = col_names[0]

        if not y_axis and ncols >= 2:
            y_axis = col_names[1]

        if not s_axis and ncols >= 3:
            s_axis = col_names[2]

        if not x_axis in col_names:
            die('--x_axis "{}" not in {}'.format(x_axis, ', '.join(col_names)))

        if not y_axis in col_names:
            die('--y_axis "{}" not in {}'.format(y_axis, ', '.join(col_names)))

        if not s_axis in col_names:
            die('--s_axis "{}" not in {}'.format(s_axis, ', '.join(col_names)))


        if args.x_exclude:
            for exclude in args.x_exclude:
                df.drop(df[df[x_axis] == exclude].index, inplace=True)

        if args.y_exclude:
            for exclude in args.y_exclude:
                df.drop(df[df[y_axis] == exclude].index, inplace=True)

        x_label = args.x_label or x_axis
        y_label = args.y_label or y_axis

        if args.sort:
            df.sort_values(by=[y_axis, x_axis],
                           ascending=[False, False],
                           inplace=True)

        x = df[x_axis]
        y = df[y_axis]
        img_width = args.image_width or 5 + len(x.unique()) / 5
        img_height = args.image_height or len(y.unique()) / 4
        plt.figure(figsize=(img_width, img_height))
        plt.scatter(x=x, y=y, s=df[s_axis] * args.multiplier, alpha=0.5)
        plt.xticks(rotation=45, ha='right')
        #plt.yticks(rotation=45, ha='right')
        plt.gcf().subplots_adjust(bottom=.4, left=.4)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        out_file = args.outfile
        if not out_file:
            dir_name = os.path.dirname(os.path.abspath(file))
            root, _ = os.path.splitext(os.path.basename(file))
            out_file = os.path.join(dir_name, root + '.' + args.format)

        plt.savefig(out_file)

        if args.open_image:
            plt.show()

        print('Done, see "{}"'.format(out_file))


# --------------------------------------------------
if __name__ == '__main__':
    main()
