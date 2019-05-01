#!/bin/bash

set -u

export FTP_LIST=get-me
export OUT_DIR=$PWD
export NCFTPGET=/rsgrps/bhurwitz/hurwitzlab/bin/ncftpget
export PBSDIR=pbs

if [[ -d $PBSDIR ]]; then
  rm -rf $DIR/*
else
  mkdir $DIR;
fi

NUM_FILES=$(wc -l $FTP_LIST | cut -d ' ' -f 1)

if [[ $NUM_FILES -gt 0 ]]; then
  JOB_ID=$(qsub -N ftp -v OUT_DIR,FTP_LIST,NCFTPGET -j oe -o $PBSDIR ftp-get.sh)
  echo "Submitted \"$FILE\" files to job \"$JOB_ID\""
else
  echo "Can\'t find any files in \"$FTP_LIST\""
fi
