#!/bin/sh
while read line
do 
    python3 ./cpc/cpc.py -o $line "${line}.cb"
done < ./test/TARGETS 