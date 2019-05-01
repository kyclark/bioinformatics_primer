#!/bin/bash

#PBS -W group_list=bhurwitz
#PBS -q standard
#PBS -l jobtype=cluster_only
#PBS -l select=1:ncpus=2:mem=4gb
#PBS -l walltime=01:00:00
#PBS -l cput=01:00:00

echo "Hello from sunny \"$(hostname)\"!"
