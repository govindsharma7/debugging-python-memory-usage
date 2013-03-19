#!/bin/bash

output_file="output_$1.txt"

echo "RSS S TTY TIME COMMAND" > $output_file

for i in `seq 1 1 2056`;
do
    python $1 $i 2>&1 &
    pid=$!
    sleep 0.2
    ps -e -O rss | grep $pid | grep python | awk '{$1 =""; print }' >> $output_file
    kill $pid
done
