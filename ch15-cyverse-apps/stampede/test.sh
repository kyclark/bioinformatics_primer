#!/bin/bash

#SBATCH -A iPlant-Collabs
#SBATCH -p development
#SBATCH -t 02:00:00
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -J lc-test

set -u

./run.sh -i "$PWD/../singularity" -p 5
