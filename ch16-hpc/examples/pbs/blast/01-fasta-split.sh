#!/bin/bash

#PBS -l jobtype=cluster_only
#PBS -l select=1:ncpus=1:mem=1gb
#PBS -l place=pack:shared
#PBS -l walltime=24:00:00
#PBS -l cput=24:00:00

set -u

cd "$CWD"
source "$CONFIG"
source "common.sh"

TMP_FILES=$(mktemp)
find "$FASTA_DIR" -type f > $TMP_FILES
NUM_FILES=$(lc "$TMP_FILES")

if [[ $NUM_FILES -lt 1 ]]; then
  echo "Found no files in FASTA_DIR \"$FASTA_DIR\""
  exit 1
fi

echo "Started splitting $(date)"

./workers/fasta-split.pl6 --in-dir="$FASTA_DIR" --out-dir="$OUT_DIR/split" 

#while read FILE; do
#  /rsgrps/bhurwitz/hurwitzlab/bin/faSplit about $FILE ${MAX_FASTA_SIZE:-100000000} "$SPLIT_DIR" 
#done < $TMP_FILES

rm $TMP_FILES

echo "Done splitting $(date)"
