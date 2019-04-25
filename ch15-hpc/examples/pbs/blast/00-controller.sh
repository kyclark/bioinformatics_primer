#!/bin/bash

set -u

if [[ $(hostname) != 'service0' ]]; then
  echo "Please ssh to service0 to submit this 'cluster_only' job."
  exit 1
fi

FASTA_DIR=""
OUT_DIR=""
QUEUE="standard" 
GROUP="bhurwitz"
RUN_STEP=""
MAIL_USER=""
MAIL_TYPE="bea"

function HELP() {
  printf "Usage:\n  %s -f FASTA_DIR -b BLAST_DB -o OUT_DIR\n\n" $(basename $0)

  echo "Required arguments:"
  echo " -b BLAST_DB"
  echo " -f FASTA_DIR"
  echo " -o OUT_DIR"
  echo ""
  echo "Options (default in parentheses):"
  echo " -g GROUP ($GROUP)"
  echo " -q QUEUE ($QUEUE)"
  echo " -r RUN_STEP"
  echo " -e MAIL_USER"
  echo ""
  exit 0
}

if [[ $# -eq 0 ]]; then
  HELP
fi

while getopts :b:e:f:g:o:q:r:h OPT; do
  case $OPT in
    b)
      BLAST_DB="$OPTARG"
      ;;
    e)
      MAIL_USER="$OPTARG"
      ;;
    f)
      FASTA_DIR="$OPTARG"
      ;;
    g)
      GROUP="$OPTARG"
      ;;
    h)
      HELP
      ;;
    o)
      OUT_DIR="$OPTARG"
      ;;
    q)
      QUEUE="$OPTARG"
      ;;
    r)
      RUN_STEP="$OPTARG"
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

#
# Check args
#
if [[ ${#BLAST_DB} -lt 1 ]]; then
  echo "Error: No BLAST_DB specified."
  exit 1
fi

if [[ ${#FASTA_DIR} -lt 1 ]]; then
  echo "Error: No FASTA_DIR specified."
  exit 1
fi

if [[ ${#OUT_DIR} -lt 1 ]]; then
  echo "Error: No OUT_DIR specified." 
  exit 1
fi

if [[ ! -d "$FASTA_DIR" ]]; then
  echo "Error: FASTA_DIR \"$FASTA_DIR\" does not exist." 
  exit 1
fi

if [[ ! -d "$OUT_DIR" ]]; then
  mkdir -p "$OUT_DIR"
fi

PBS_DIR="pbs"
if [[ ! -d "$PBS_DIR" ]]; then
  mkdir -p "$PBS_DIR"
fi

#
# You must export any variables you want to send with "-v"
#
export CONFIG="$$.conf"
export CWD=$(pwd)

#
# An alternate way to send information to the compute nodes
# is to write them to a file that you can "source"
#
echo "export BLAST_DB=$BLAST_DB"    > $CONFIG
echo "export FASTA_DIR=$FASTA_DIR" >> $CONFIG
echo "export OUT_DIR=$OUT_DIR"     >> $CONFIG

PREV_JOB_ID=""
i=0

for STEP in $(ls 0[1-9]*.sh); do
  let i++

  if [[ ${#RUN_STEP} -gt 0 ]] && [[ $(basename $STEP) != $RUN_STEP ]]; then
    continue
  fi

  STEP_NAME=$(basename $STEP '.sh')
  ARGS="-q $QUEUE -W group_list=$GROUP -N $STEP_NAME -j oe -o $CWD/$PBS_DIR -v CWD,CONFIG"

  if [[ ${#MAIL_USER} -gt 0 ]]; then
    ARGS="$ARGS -M $MAIL_USER -m $MAIL_TYPE"
  fi

  if [[ ${#PREV_JOB_ID} -gt 0 ]]; then
    ARGS="$ARGS -W depend=afterok:$PREV_JOB_ID"
  fi

  CMD="qsub $ARGS $CWD/$STEP"
  JOB_ID=$($CMD)

  if [[ ${#JOB_ID} -lt 1 ]]; then 
    echo Failed to get JOB_ID from \"$CMD\"
    exit 1
  fi
  
  printf "%3d: %s [%s]\n" $i $STEP $JOB_ID

  PREV_JOB_ID=$JOB_ID
done

echo Done.
