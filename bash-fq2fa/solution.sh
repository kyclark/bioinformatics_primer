#!/bin/bash

# Convert FASTQ files to FASTA
# Author: Ken Youens-Clark <kyclark@gmail.com>

set -u

INPUT=""
OUT_DIR=""
NO_CLOBBER=0

function USAGE() {
    printf "Usage:\\n  %s -i INPUT -o OUTDIR\\n\\n" "$(basename "$0")"

    echo "Required arguments:"
    echo " -i INPUT (DIR/FILE[s])"
    echo " -o OUTDIR (DIR/FILE[s])"
    echo
    exit "${1:-0}"
}

[[ $# -eq 0 ]] && USAGE 1

while getopts :i:o:nh OPT; do
    case $OPT in
        i)
            INPUT="$OPTARG"
            ;;
        h)
            USAGE
            ;;
        n)
            NO_CLOBBER=1
            ;;
        o)
            OUT_DIR="$OPTARG"
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

[[ -z "$INPUT" ]] && USAGE 1
[[ ! -d "$OUT_DIR" ]] && mkdir -p "$OUT_DIR"

INPUT_FILES=$(mktemp)
[[ -f "$INPUT" ]] && echo "$INPUT" > "$INPUT_FILES"
[[ -d "$INPUT" ]] && find "$INPUT" -type f > "$INPUT_FILES"

NUM_INPUT=$(wc -l "$INPUT_FILES" | awk '{print $1}')
if [[ $NUM_INPUT -lt 1 ]]; then
    echo "No input"
    exit 1
fi

JOBS=$(mktemp)

i=0
while read -r FILE; do
    i=$((i+1))
    BASENAME=$(basename "$FILE")
    BASENAME=${BASENAME%%.*}

    printf "%3d: %s\\n" $i "$BASENAME"

    OUT_FILE="$OUT_DIR/$BASENAME.fa"
    if [[ -s "$OUT_FILE" ]] && [[ $NO_CLOBBER -gt 0 ]]; then
        echo "OUT_FILE \"$OUT_FILE\" already exists"
        continue
    fi

    echo "fq2fa.awk \"$FILE\" > \"$OUT_FILE\"" >> "$JOBS"
done < "$INPUT_FILES"

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
