#!/bin/bash

#SBATCH -A iPlant-Collabs
#SBATCH -N 1
#SBATCH -n 4
#SBATCH -t 24:00:00
#SBATCH -p normal
#SBATCH -J imicrobe
#SBATCH --mail-type BEGIN,END,FAIL
#SBATCH --mail-user kyclark@email.arizona.edu

LAUNCHER_DIR="$HOME/src/launcher"
PARAM="reads.txt"

module load launcher
module load irods

echo "Starting parallel job... $(date)"
export LAUNCHER_DIR=$HOME/src/launcher
export LAUNCHER_PPN=4
export LAUNCHER_WORKDIR=$OUT_DIR
time $LAUNCHER_DIR/paramrun SLURM $LAUNCHER_DIR/init_launcher $LAUNCHER_WORKDIR $PARAM
echo "Finished parallel $(date)"
rm $PARAM
