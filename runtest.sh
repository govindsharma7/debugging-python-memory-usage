#!/bin/bash

echo "RSS S TTY TIME COMMAND" > output.txt

for i in `seq 1 200`;
do
    python debug_memory.py $i 2>&1 &
    pid=$!
    sleep 0.2
    ps -e -O rss | grep $pid | grep python | cut -d " " -f 2- >> output.txt
    kill $pid
done
