#!/bin/bash

#SBATCH -A iPlant-Collabs
#SBATCH -p normal
#SBATCH -t 10:00:00
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -J fq2fa
#SBATCH --mail-user=kyclark@email.arizona.edu
#SBATCH --mail-type=BEGIN,END,FAIL

module load fastx_toolkit

set -u

function HELP() {
  STATUS=${1:-0}
  printf "Usage:\n  %s -i IN_DIR [-o OUT_DIR] [-q]\n" $(basename $0)
  echo 
  echo "Required arguments:"
  echo " -i IN_DIR"
  echo "Options:"
  echo " -o OUT_DIR (default same as IN_DIR)"
  echo " -q (use 'Q33')"
  echo 
  exit $STATUS
}

function lc() {
    wc -l $1 | cut -d ' ' -f 1
}

if [[ $# -lt 1 ]]; then
  HELP
fi

IN_DIR=""
OUT_DIR=""
Q33=""

while getopts :i:o:qh OPT; do
  case $OPT in
    i)
      IN_DIR="$OPTARG"
      ;;
    o)
      OUT_DIR="$OPTARG"
      ;;
    h)
      HELP
      ;;
    q)
      Q33=1
      ;;
    :)
      echo "Error: Option -$OPTARG requires an argument."
      exit 1
      ;;
    \?)
      echo "Error: Invalid option: -${OPTARG:-""}"
      exit 1
  esac
done

if [[ ${#IN_DIR} -lt 1 ]]; then
  echo "Missing IN_DIR"
  HELP 1
fi

if [[ ! -d $IN_DIR ]]; then
  echo "IN_DIR \"$IN_DIR\""
  HELP 1
fi

if [[ ${#OUT_DIR} -lt 1 ]]; then
  OUT_DIR=$IN_DIR
fi

TMP_FILES=$(mktemp)
find $IN_DIR -type f -name \*.fastq > $TMP_FILES
NUM_FILES=$(lc $TMP_FILES)

if [[ $NUM_FILES -lt 1 ]]; then
  echo "Found nothing in IN_DIR \"$IN_DIR\""
  HELP 1
fi

ARGS=""
if [[ $Q33 -gt 0 ]]; then
  ARGS="-Q33"
fi

PARAM="$$.param"

i=0
while read FILE; do
  let i++
  BASENAME=$(basename $FILE)
  BASENAME=${BASENAME%.*} # remove extension

  printf "%3d: %s\n" $i $BASENAME

  echo "fastq_to_fasta $ARGS -i $FILE -o $OUT_DIR/$BASENAME.fa" >> $PARAM
done < $TMP_FILES

echo "Starting launcher $(date)"
export LAUNCHER_DIR="$HOME/src/launcher"
export LAUNCHER_PLUGIN_DIR=$LAUNCHER_DIR/plugins
export LAUNCHER_RMI=SLURM
export LAUNCHER_JOB_FILE=$PARAM

$LAUNCHER_DIR/paramrun
echo "Ended launcher $(date)"

rm $TMP_FILES
rm $PARAM

echo Done.
