#!/bin/bash

#PBS -l jobtype=cluster_only
#PBS -l select=1:ncpus=1:mem=1gb
#PBS -l place=pack:shared
#PBS -l walltime=24:00:00
#PBS -l cput=24:00:00

set -u

cd $CWD
source $CONFIG
source common.sh

SPLIT_DIR="$OUT_DIR/split"

if [[ ! -d "$SPLIT_DIR" ]]; then
  echo "Cannot find SPLIT_DIR \"$SPLIT_DIR\""
  exit 1
fi

TMP_FILES=$(mktemp)
find "$SPLIT_DIR" -type f > $TMP_FILES
NUM_FILES=$(lc $TMP_FILES)

if [[ $NUM_FILES -lt 1 ]]; then
  echo "Found no files in SPLIT_DIR \"$SPLIT_DIR\""
  exit 1
fi

BLAST_OUT="$OUT_DIR/blast-out"

if [[ ! -d "$BLAST_OUT" ]]; then
  mkdir -p "$BLAST_OUT"
fi

echo "Started BLAST $(date)"

module load blast

i=0
while read FILE; do
  let i++
  BASENAME=$(basename $FILE)
  printf "%5d: %s\n" $i 

  OUT_FILE="$BLAST_OUT/$BASENAME"

  blastn -query "$FILE" -out "$OUT_FILE" -outfmt 6 -db $BLAST_DB
done < $TMP_FILES

rm $TMP_FILES

echo "Done BLAST $(date)"
