#!/bin/bash

set -u

export FTP_LIST=get-me
export OUT_DIR=$PWD
export NCFTPGET=/rsgrps/bhurwitz/hurwitzlab/bin/ncftpget
export STEP_SIZE=2
export PBS_DIR=pbs

if [[ -d $PBS_DIR ]]; then
  rm -rf $PBS_DIR/*
else
  mkdir $PBS_DIR;
fi

NUM_FILES=$(wc -l $FTP_LIST | cut -d ' ' -f 1)

if [[ $NUM_FILES -lt 1 ]]; then
  echo "Can\'t find any files in \"$FTP_LIST\""
  exit 1
fi

JOBS=""
if [[ $NUM_FILES -gt 1 ]]; then
  JOBS="-J 1-$NUM_FILES"
  if [[ $STEP_SIZE -gt 1 ]]; then
    JOBS="$JOBS:$STEP_SIZE"
  fi
fi

JOB_ID=$(qsub $JOBS -N ftp -v OUT_DIR,STEP_SIZE,FTP_LIST,NCFTPGET -j oe -o $PBS_DIR ftp-get.sh)

echo "Submitted \"$NUM_FILES\" files to job \"$JOB_ID\""
