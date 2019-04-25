#!/bin/bash

#SBATCH -A iPlant-Collabs
#SBATCH -p development # or "normal"
#SBATCH -t 01:00:00
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -J hello
#SBATCH --mail-user=kyclark@email.arizona.edu
#SBATCH --mail-type=BEGIN,END,FAIL

echo "Hello from sunny \"$(hostname)\"!"
