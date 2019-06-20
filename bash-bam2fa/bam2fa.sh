#!/usr/bin/env bash
# Convert BAM files to FASTA

set -u

# Check number of arguments
if [[ $# -lt 2 ]] || [[ $# -gt 3 ]]; then
    echo "Usage: $(basename "$0") IN_DIR OUT_DIR [CORES]" 
    exit 1
fi

# Assign arguments into named variable
IN_DIR=$1
OUT_DIR=$2
CORES=${3:-40} # default

# Check input directory
if [[ ! -d "$IN_DIR" ]]; then
    echo "Bad IN_DIR \"$IN_DIR\""
    exit 1
fi

# Make output directory if necessary
[[ ! -d "$OUT_DIR" ]] && mkdir -p "$OUT_DIR"

# Find, check input files
FILES=$(mktemp)
find "$IN_DIR" -name \*.bam -size +0c > "$FILES"
NUM=$(wc -l "$FILES" | awk '{print $1}')
if [[ $NUM -lt 1 ]]; then
    echo "No BAM files in IN_DIR \"$IN_DIR\""
    exit 1
fi

# Iterate BAM file in input directory, create samtools command
JOBS=$(mktemp)
i=0
while read -r BAM; do
    i=$((i+1))
    BASE=$(basename "$BAM" ".bam")
    printf "%3d: %s\\n" $i "$BASE"

    # Only process if FASTA does not exist
    FASTA="$OUT_DIR/$BASE.fa"
    if [[ ! -f "$FASTA" ]]; then
        echo "samtools fasta \"$BAM\" > \"$FASTA\"" >> "$JOBS"
    fi
done < "$FILES"

# Look for parallel
PARALLEL=$(which parallel)
if [[ -z "$PARALLEL" ]]; then
    echo "Running serially, install GNU parallel for speed!"
    sh "$JOBS"
else
    echo "Running with $CORES cores in parallel"
    parallel -j "$CORES" --halt soon,fail=1 < "$JOBS"
fi

# Remove temp files, exit
rm "$FILES"
rm "$JOBS"
echo "Done."
