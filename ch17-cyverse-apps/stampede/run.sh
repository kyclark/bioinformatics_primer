#!/bin/bash

#SBATCH -J lc
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p normal
#SBATCH -t 24:00:00
#SBATCH -A iPlant-Collabs

module load tacc-singularity
module load launcher

set -u

INPUT=""
PVALUE="0.01"
IMG="lc.img"

#
# These are for the LAUNCHER. Ignore unless you need to parallelize 
# jobs. TACC_LAUNCHER_DIR will be imported into your $ENV once you 
# "module load launcher"
#
PARAMRUN="$TACC_LAUNCHER_DIR/paramrun"
export LAUNCHER_PLUGIN_DIR="$TACC_LAUNCHER_DIR/plugins"
export LAUNCHER_WORKDIR="$PWD"
export LAUNCHER_RMI="SLURM"
export LAUNCHER_SCHED="interleaved"

function USAGE() {
    printf "Usage:\n  %s -i INPUT [-p PVALUE]\n\n" "$(basename "$0")"

    echo "Required arguments:"
    echo " -i INPUT"
    echo ""
    echo "Options:"
    echo " -p PVALUE ($PVALUE)"
    echo ""
    exit "${1:-0}"
}

[[ $# -eq 0 ]] && USAGE 1

while getopts :i:p:h OPT; do
    case $OPT in
        i)
            INPUT="$OPTARG"
            ;;
        h)
            USAGE
            ;;
        p)
            PVALUE="$OPTARG"
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

if [[ -z "$INPUT" ]]; then
    echo "-i INPUT is required"
    exit 1
fi

if [[ ! -f "$IMG" ]]; then
    echo "Missing IMG \"$IMG\""
    exit 1
fi

#
# Detect if INPUT is a regular file or directory, expand to list of files
#
INPUT_FILES=$(mktemp)
if [[ -f "$INPUT" ]]; then
    echo "$INPUT" > "$INPUT_FILES"
elif [[ -d "$INPUT" ]]; then
    find "$INPUT" -type f > "$INPUT_FILES"
else
    echo "-i \"$INPUT\" is neither file nor directory"
    exit 1
fi

NUM_INPUT=$(wc -l "$INPUT_FILES" | awk '{print $1}')
if [[ $NUM_INPUT -lt 1 ]]; then
    echo "There are no files to process."
    exit 1
fi

echo "I will process NUM_INPUT \"$NUM_INPUT\" at PVALUE \"$PVALUE\""
cat -n "$INPUT_FILES"

#
# Here is how to use LAUNCHER for parallelization
#
PARAM="$$.param"
cat /dev/null > "$PARAM"
while read -r FILE; do
    echo "singularity exec $IMG lc.py $FILE" >> "$PARAM"
done < "$INPUT_FILES"

echo "Starting Launcher"
if [[ $NUM_INPUT -lt 16 ]]; then
    LAUNCHER_PPN=$NUM_INPUT
else
    LAUNCHER_PPN=16
fi

LAUNCHER_JOB_FILE="$PARAM"
export LAUNCHER_JOB_FILE
export LAUNCHER_PPN
$PARAMRUN
echo "Ended LAUNCHER"
unset LAUNCHER_PPN

rm "$PARAM"

echo "Done."
