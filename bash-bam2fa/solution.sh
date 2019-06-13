#!/usr/bin/env bash

# Convert BAM files to FASTA
# Author: Ken Youens-Clark <kyclark@gmail.com>

set -u

if [[ $# -lt 1 ]] || [[ $# -gt 3 ]]; then
    echo "Usage: $(basename "$0") IN_DIR OUT_DIR [CORES]" 
    exit 1
fi

IN_DIR=$1
OUT_DIR=$2
CORES=${3:-40}

if [[ ! -d "$IN_DIR" ]]; then
    echo "Bad IN_DIR \"$IN_DIR\""
    exit 1
fi

[[ ! -d "$OUT_DIR" ]] && mkdir -p "$OUT_DIR"

JOBS=$(mktemp)
i=0
for BAM in $IN_DIR/*.bam; do
    i=$((i+1))
    BASE=$(basename "$BAM" ".bam")
    printf "%3d: %s\\n" $i "$BASE"

    # Only process if FASTA does not exist
    FASTA="$OUT_DIR/$BASE.fa"
    if [[ ! -f "$FASTA" ]]; then
        echo "samtools fasta \"$BAM\" > \"$FASTA\"" >> "$JOBS"
    fi
done

PARALLEL=$(which parallel)

if [[ -z "$PARALLEL" ]]; then
    echo "Running serially, install GNU parallel for speed!"
    sh "$JOBS"
else
    echo "Running with $CORES cores in parallel"
    parallel -j "$CORES" --halt soon,fail=1 < "$JOBS"
fi

rm "$JOBS"
echo "Done."
