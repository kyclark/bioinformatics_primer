#!/usr/bin/env bash
# Convert BAM files to FASTA

set -u

# Check number of arguments
if [[ $# -lt 2 ]] || [[ $# -gt 3 ]]; then
    echo "Usage: $(basename "$0") INPUT OUT_DIR [CORES]" 
    exit 1
fi

# Assign arguments into named variable
INPUT=$1
OUT_DIR=$2
CORES=${3:-40} # default


# Find input files
FILES=$(mktemp)
if [[ -f "$INPUT" ]]; then
    echo "$INPUT" > "$FILES"
elif [[ -d "$INPUT" ]]; then
    find "$INPUT" -name \*.bam -size +0c > "$FILES"
else
    echo "INPUT \"$INPUT\" neither file nor directory!"
    exit 1
fi

# Check that we have input
NUM=$(wc -l "$FILES" | awk '{print $1}')
if [[ $NUM -lt 1 ]]; then
    echo "No BAM files in IN_DIR \"$IN_DIR\""
    exit 1
fi

# Make output directory if necessary
[[ ! -d "$OUT_DIR" ]] && mkdir -p "$OUT_DIR"

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
echo "Done, see output in \"$OUT_DIR\""
