#!/bin/sh
while read line
do 
    python3 ./cpc/cpc.py -L./lib -o "./test/${line}" "./test/${line}.cb" --dump-ast
done < ./test/TARGETS 