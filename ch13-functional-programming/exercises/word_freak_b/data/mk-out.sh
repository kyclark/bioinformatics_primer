#!/usr/bin/env bash

PRG=../freak.py

for FILE in usdeclar.txt const.txt nobody.txt; do
    for MIN in 0 5 10; do
        for SORT in word frequency; do
            $PRG -m $MIN -s $SORT $FILE > $FILE.$MIN.$SORT.out
        done
    done
done

for MIN in 0 5 10; do
    for SORT in word frequency; do
        $PRG -m $MIN -s $SORT usdeclar.txt const.txt nobody.txt > all.$MIN.$SORT.out
    done
done
