#!/bin/sh
while read line
do 
    python3 ./cpc/cpc.py -o "./test/${line}" "./test/${line}.cb"
done < ./test/TARGETS 