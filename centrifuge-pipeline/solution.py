#!/usr/bin/env python3
"""Run Centrifuge"""

import argparse
import os
import re
import subprocess
import sys
import tempfile as tmp


# --------------------------------------------------
def get_args():
    """Get command-line args"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-q',
        '--query',
        help='File or directory of input',
        metavar='str',
        type=str,
        action='append',
        required=True)

    parser.add_argument(
        '-r',
        '--reads_are_paired',
        help='Expect forward/reverse (1/2) reads in --query',
        action='store_true')

    parser.add_argument(
        '-f',
        '--format',
        help='Input file format',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-i',
        '--index',
        help='Centrifuge index name',
        metavar='str',
        type=str,
        default='p_compressed+h+v')

    parser.add_argument(
        '-I',
        '--index_dir',
        help='Centrifuge index directory',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--out_dir',
        help='Output directory',
        metavar='str',
        type=str,
        default=os.path.join(os.getcwd(), 'centrifuge-out'))

    parser.add_argument(
        '-x',
        '--exclude_tax_ids',
        help='Comma-separated list of tax ids to exclude',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-T',
        '--figure_title',
        help='Title for the bubble chart',
        metavar='str',
        type=str,
        default='Species abundance by sample')

    parser.add_argument(
        '-t',
        '--threads',
        help='Num of threads per instance of centrifuge',
        metavar='int',
        type=int,
        default=1)

    parser.add_argument(
        '-P',
        '--procs',
        help='Max number of processes to run',
        metavar='int',
        type=int,
        default=4)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start here"""

    args = get_args()
    out_dir = args.out_dir
    index_dir = args.index_dir
    index_name = args.index
    file_format = args.format

    if not index_dir:
        print('--index_dir is required')
        sys.exit(1)

    if not index_name:
        print('--index_name is required')
        sys.exit(1)

    if not os.path.isdir(index_dir):
        die('--index_dir "{}" is not a directory'.format(index_dir))

    valid_index = set(
        map(lambda s: re.sub(r'\.\d+\.cf$', '', os.path.basename(s)),
            os.listdir(index_dir)))

    if not index_name in valid_index:
        tmpl = '--index "{}" is not valid, please choose from: {}'
        die(tmpl.format(index_name, ', '.join(sorted(valid_index))))

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    input_files = find_input_files(args.query, args.reads_are_paired)

    if not file_format:
        exts = set()
        for direction in input_files:
            for file in input_files[direction]:
                base = re.sub(r'\.gz$', '', os.path.basename(file))
                _, ext = os.path.splitext(base)
                exts.add(re.sub(r'^\.', '', ext))

        guesses = set()
        for ext in exts:
            if re.match(r'f(?:ast|n)?a', ext):
                guesses.add('fasta')
            elif re.match(r'f(?:ast)?q', ext):
                guesses.add('fastq')

        if len(guesses) == 1:
            file_format = guesses.pop()
        else:
            msg = 'Cannot guess file format ({}) from extentions ({})'
            die(msg.format(', '.join(guesses), ', '.join(exts)))

    valid_format = set(['fasta', 'fastq'])
    if not file_format in valid_format:
        msg = '--format "{}" is not valid, please choose from {}'
        die(msg.format(file_format, ', '.join(valid_format)))

    msg = 'Files found: forward = "{}", reverse = "{}", unpaired = "{}"'
    print(
        msg.format(
            len(input_files['forward']), len(input_files['reverse']),
            len(input_files['unpaired'])))

    reports_dir = run_centrifuge(
        file_format=file_format,
        files=input_files,
        out_dir=out_dir,
        exclude_tax_ids=args.exclude_tax_ids,
        index_dir=index_dir,
        index_name=index_name,
        threads=args.threads,
        procs=args.procs)

    fig_dir = make_bubble(
        reports_dir=reports_dir, out_dir=out_dir, title=args.figure_title)

    print('Done, reports in "{}", figures in "{}"'.format(
        reports_dir, fig_dir))


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""

    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something went wrong'):
    """Print a message to STDERR and exit with error"""

    warn('Error: {}'.format(msg))
    sys.exit(1)


# --------------------------------------------------
def unique_extensions(files):
    exts = set()
    for file in files:
        _, ext = os.path.splitext(file)
        exts.add(ext[1:])  # skip leading "."

    return exts


# --------------------------------------------------
def find_input_files(query, reads_are_paired):
    """Find input files from list of files/dirs"""

    files = []
    for qry in query:
        if os.path.isdir(qry):
            for filename in os.scandir(qry):
                if filename.is_file():
                    files.append(filename.path)
        elif os.path.isfile(qry):
            files.append(qry)
        else:
            die('--query "{}" neither file nor directory'.format(qry))

    files.sort()  # inplace

    forward = []
    reverse = []
    unpaired = []

    if reads_are_paired:
        extensions = unique_extensions(files)
        re_tmpl = '.+[_-][Rr]?{}\.(?:' + '|'.join(extensions) + ')$'
        forward_re = re.compile(re_tmpl.format('1'))
        reverse_re = re.compile(re_tmpl.format('2'))

        for fname in files:
            if forward_re.search(fname):
                forward.append(fname)
            elif reverse_re.search(fname):
                reverse.append(fname)
            else:
                unpaired.append(fname)

        num_forward = len(forward)
        num_reverse = len(reverse)

        if num_forward and num_reverse and num_forward != num_reverse:
            msg = 'Number of forward ({}) and reverse ({}) reads do not match'
            die(msg.format(num_forward, num_reverse))

    else:
        unpaired = files

    return {'forward': forward, 'reverse': reverse, 'unpaired': unpaired}


# --------------------------------------------------
def line_count(fname):
    """Count the number of lines in a file"""

    n = 0
    for _ in open(fname):
        n += 1

    return n


# --------------------------------------------------
def run_job_file(jobfile, msg='Running job', procs=1):
    """Run a job file if there are jobs"""

    num_jobs = line_count(jobfile)
    warn('{} (# jobs = {})'.format(msg, num_jobs))

    if num_jobs > 0:
        cmd = 'parallel --halt soon,fail=1 -P {} < {}'.format(procs, jobfile)

        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            die('Error:\n{}\n{}\n'.format(err.stderr, err.stdout))
        finally:
            os.remove(jobfile)

    return True


# --------------------------------------------------
def run_centrifuge(**args):
    """Run Centrifuge"""

    file_format = args['file_format']
    files = args['files']
    exclude_ids = get_excluded_tax(args['exclude_tax_ids'])
    index_name = args['index_name']
    index_dir = args['index_dir']
    out_dir = args['out_dir']
    threads = args['threads']
    procs = args['procs']

    reports_dir = os.path.join(out_dir, 'reports')

    if not os.path.isdir(reports_dir):
        os.makedirs(reports_dir)

    jobfile = tmp.NamedTemporaryFile(delete=False, mode='wt')
    exclude_arg = '--exclude-taxids ' + exclude_ids if exclude_ids else ''
    format_arg = '-f' if file_format == 'fasta' else ''

    cmd_tmpl = 'CENTRIFUGE_INDEXES={} centrifuge {} {} -p {} -x {} '
    cmd_base = cmd_tmpl.format(index_dir, exclude_arg, format_arg, threads,
                               index_name)

    for file in files['unpaired']:
        basename = os.path.basename(file)
        tsv_file = os.path.join(reports_dir, basename + '.tsv')
        sum_file = os.path.join(reports_dir, basename + '.sum')
        tmpl = cmd_base + '-U "{}" -S "{}" --report-file "{}"\n'
        if not os.path.isfile(tsv_file):
            jobfile.write(tmpl.format(file, sum_file, tsv_file))

    for i, file in enumerate(files['forward']):
        basename = os.path.basename(file)
        tsv_file = os.path.join(reports_dir, basename + '.tsv')
        sum_file = os.path.join(reports_dir, basename + '.sum')
        tmpl = cmd_base + '-1 "{}" -2 "{}" -S "{}" --report-file "{}"\n'
        if not os.path.isfile(tsv_file):
            jobfile.write(
                tmpl.format(file, files['reverse'][i], sum_file, tsv_file))

    jobfile.close()

    run_job_file(jobfile=jobfile.name, msg='Running Centrifuge', procs=procs)

    return reports_dir


# --------------------------------------------------
def get_excluded_tax(ids):
    """Verify the ids look like numbers"""

    tax_ids = []

    if ids:
        for s in [x.strip() for x in ids.split(',')]:
            if s.isnumeric():
                tax_ids.append(s)
            else:
                warn('tax_id "{}" is not numeric'.format(s))

    return ','.join(tax_ids)


# --------------------------------------------------
def make_bubble(reports_dir, out_dir, title):
    """Make bubble chart"""

    fig_dir = os.path.join(out_dir, 'figures')

    if not os.path.isdir(fig_dir):
        os.makedirs(fig_dir)

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    bubble = os.path.join(cur_dir, 'centrifuge_bubble.r')
    tmpl = '{} --dir "{}" --title "{}" --outdir "{}"'
    job = tmpl.format(bubble, reports_dir, title, fig_dir)
    warn(job)

    subprocess.run(job, shell=True)

    return fig_dir


# --------------------------------------------------
if __name__ == '__main__':
    main()
