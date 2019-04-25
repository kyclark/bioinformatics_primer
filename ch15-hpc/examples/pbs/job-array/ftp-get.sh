#!/bin/bash

#PBS -W group_list=bhurwitz
#PBS -q standard
#PBS -l jobtype=serial
#PBS -l select=1:ncpus=2:mem=4gb
#PBS -l place=pack:shared
#PBS -l walltime=24:00:00
#PBS -l cput=24:00:00

set -u

echo "Started $(date)"

cd $OUT_DIR

TMP_FILES=$(mktemp)
sed -n "${PBS_ARRAY_INDEX:-1},${STEP_SIZE:-1}" $FTP_FILES > $TMP_FILES
NUM_FILES=$(wc -l $TMP_FILES | cut -d ' ' -f 1)

if [[ $NUM_FILES -lt 1 ]]; then
  echo "Failed to fetch files"
  exit 1
fi

echo "Will fetch $NUM_FILES"

i=0
while read FTP; do
  let i++
  printf "%3d: %s\n" $i $FTP
  $NCFTPGET $FTP
done < $TMP_FILES

echo "Ended $(date)"
