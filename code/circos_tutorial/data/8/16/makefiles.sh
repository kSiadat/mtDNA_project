#!/bin/bash

for i in `seq 0 15` ; do

echo $i
cat histogram.txt | awk ' BEGIN {srand()} { print $1,$2,$3,rand() } ' > histogram.$i.txt
sleep 1

done
