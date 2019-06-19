#!/usr/bin/env bash

set -u

PRG="./parse_gff.py"
OUT_DIR="test-outs"
GFF1="../inputs/HUMANGUT_SMPL_INB.fa.prodigal.gff"
GFF2="../inputs/mgm4529847.3.050.upload.fna.prodigal.gff"

[[ ! -d "$OUT_DIR" ]] && mkdir -p "$OUT_DIR"

$PRG "$GFF1" > "$OUT_DIR/gff1.noargs"
$PRG "$GFF1" -m 100 > "$OUT_DIR/gff1.min100"
$PRG "$GFF1" -m 300 > "$OUT_DIR/gff1.min300"
$PRG "$GFF2" > "$OUT_DIR/gff2.noargs"
$PRG "$GFF2" -m 125 > "$OUT_DIR/gff2.min125"
