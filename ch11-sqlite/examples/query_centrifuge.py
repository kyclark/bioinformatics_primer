#!/usr/bin/env python3
"""Query centrifuge.db for NCBI tax id"""

import argparse
import os
import re
import sys
import sqlite3
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(description='Argparse Python script')
    parser.add_argument('-d', '--dbname', help='Centrifuge db name',
                        metavar='str', type=str, default='centrifuge.db')
    parser.add_argument('-o', '--orderby', help='Order by',
                        metavar='str', type=str, default='abundance')
    parser.add_argument('-s', '--sortorder', help='Sort order',
                        metavar='str', type=str, default='desc')
    parser.add_argument('-t', '--taxid', help='NCBI taxonomy id',
                        metavar='str', type=str, required=True)
    return parser.parse_args()

# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    dbname = args.dbname
    order_by = args.orderby
    sort_order = args.sortorder

    if not os.path.isfile(dbname):
        print('"{}" is not a valid file'.format(dbname))
        sys.exit(1)

    flds = set(['tax_name', 'num_reads', 'abundance', 'sample_name'])
    if not order_by in flds:
        print('"{}" not an allowed --orderby, choose from {}'.format(
            order_by, ', '.join(flds)))
        sys.exit(1)

    sorting = set(['asc', 'desc'])
    if not sort_order in sorting:
        print('"{}" not an allowed --sortorder, choose from {}'.format(
            order_by, ', '.join(sorting)))
        sys.exit(1)

    tax_ids = []
    for tax_id in re.split(r'\s*,\s*', args.taxid):
        if re.match(r'^\d+$', tax_id):
            tax_ids.append(tax_id)
        else:
            print('"{}" does not look like an NCBI tax id'.format(tax_id))

    if len(tax_ids) == 0:
        print('No tax ids')
        sys.exit(1)

    db = sqlite3.connect(dbname)
    cur = db.cursor()
    sql = """
        select   s.sample_name, t.tax_name, s2t.num_reads, s2t.abundance
        from     sample s, tax t, sample_to_tax s2t
        where    s.sample_id=s2t.sample_id
        and      s2t.tax_id=t.tax_id
        and      t.ncbi_id in ({})
        order by {} {}
    """.format(', '.join(tax_ids), order_by, sort_order)

    cur.execute(sql)

    samples = cur.fetchall()
    if len(samples) > 0:
        cols = [d[0] for d in cur.description]
        print(tabulate(samples, headers=cols))
    else:
        print('No results')

# --------------------------------------------------
if __name__ == '__main__':
    main()
