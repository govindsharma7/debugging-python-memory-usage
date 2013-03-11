#!/bin/bash

echo "PID RSS S TTY TIME COMMAND" > output.txt

for i in `seq 1 200`;
do
    python debug_memory.py "data/stuff_${i}K.txt" &
    pid=$!
    sleep 0.1
    ps -e -O rss | grep $pid | grep -v grep >> output.txt
    kill $pid
done   
