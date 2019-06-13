#!/bin/bash

# call function
echo -n "1: BASENAME: " 
basename "$0"

# put function results into variable
BASENAME=$(basename "$0")
echo "2: BASENAME: $BASENAME"

# use results of function as argument to another function
echo "3: BASENAME:" "$(basename "$0")"
echo "4: BASENAME: $(basename "$0")"
printf "5: BASENAME: %s\n" "$(basename "$0")"
