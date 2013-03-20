#!/bin/bash

output_file="output_$1.txt"

echo "RSS COMMAND" > $output_file

for j in $(seq 0 16384 262144);
do
    in_kb=$(expr $j / 1024)
    echo >> $output_file
    echo "==================================================" >> $output_file
    echo "MALLOC_MMAP_THRESHOLD_=$j ($in_kb KB)" >> $output_file
    echo "==================================================" >> $output_file

    for i in $(seq 1 1 260);
    do
        MALLOC_MMAP_THRESHOLD_=$j python $1 $i 2>&1 &
        pid=$!
        sleep 0.2
        ps -o pid,rss,cmd | grep $pid | grep python | awk '{$1=""; print}' >> $output_file
        kill $pid
    done
done
