#!/usr/bin/env bash

set -u

# List the exercices

find . -name exercises -type d | sort | while read -r DIR; 
do 
    echo $DIR 
    find $DIR -maxdepth 1 -mindepth 1 -type d | sort | while read -r EX; 
    do 
        echo "  - $(basename $EX)"
    done
done
