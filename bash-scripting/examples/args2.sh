#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "There are no arguments"
else
    i=0
    for ARG in "$@"; do
        let i++
        echo "$i: $ARG"
    done
fi
