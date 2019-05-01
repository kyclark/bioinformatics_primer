#!/bin/bash

#PBS -W group_list=bhurwitz
#PBS -q standard
#PBS -l jobtype=serial
#PBS -l select=1:ncpus=2:mem=4gb
#PBS -l place=pack:shared
#PBS -l walltime=24:00:00
#PBS -l cput=24:00:00

set -u

cd $OUT_DIR

echo "Started $(date)"

i=0
while read FTP; do
  let i++
  printf "%3d: %s\n" $i $FTP
  $NCFTPGET $FTP
done < $FTP_LIST

echo "Ended $(date)"
