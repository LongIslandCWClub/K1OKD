#!/bin/bash

function play_call {
    $(echo "$1" | awk '{ print toupper($0) }' | \
        sed 's/\(.\)/\\\1 /g' | say -r250)
}

function get_calls {
    calls=()
    IFS=$'\n' read -d '' -r -a calls < $1
}

get_calls $1
for call in ${calls[@]}; do
    repeat=1
    while [ $repeat = 1 ]; do
        play_call $call
        read -p "call? " input
        if [ $call = $input ]; then
            echo "correct!"
            repeat=0
        elif [ $input = "?" ]; then
            repeat=1 
        elif [ $input = "q" ] || [ $input = "Q" ] ||\
             [ $input = "e" ] || [ $input = "E" ]; then
            exit 0
        else 
            echo "wrong! $call =/= $input"
            repeat=0
        fi
    done
done

