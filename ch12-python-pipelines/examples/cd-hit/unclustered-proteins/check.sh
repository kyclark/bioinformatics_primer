#!/bin/bash

set -u

function lc() {
  wc -l $1 | cut -d ' ' -f 1
}

echo $(lc clustered-ids.o)   > count-clustered.o
echo $(lc unclustered-ids.o) > count-unclustered.o

bc <<< "$(cat count-clustered.o)+$(cat count-unclustered.o)" > count.o

grep -e '^>' proteins.fa | cut -d ' ' -f 1 | wc -l > proteins-count.o

MYCOUNT=$(cat count.o)
PROTCOUNT=$(cat proteins-count.o)

if [[ "$MYCOUNT" -eq "$PROTCOUNT" ]]; then
  echo "Counts match, all's good."
else
  echo "Not OK (MYCOUNT='$MYCOUNT', PROTCOUNT='$PROTCOUNT')";
fi
