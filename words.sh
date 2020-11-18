#!/bin/bash

function spell_word {
    $(echo "$1" | awk '{ print toupper($0) }' | \
        sed 's+/+stroke +g;s/[?]/question /g;s/[.]/period /g;s/[,]/comma /g;s/<BT>/break /g;s/=/break /g;s/\([A-Z0-9]\)/\\\1 /g' |
        say -r140 --quality 127 )
}

function get_words {
    words=()
    IFS=$' ' read -d '' -r -a words < $1
}

get_words $1
for word in ${words[@]}; do
    spell_word $word
    sleep 0.5
    echo -n "$(echo $word | tr [a-z] [A-Z]) "
    if [ $word = '<BT>' ] || [ $word = '=' ]; then
        echo ""
    else
        sleep 0.5
        #say -r150 --quality 127 $word
        #sleep 0.5
    fi 
done
echo 

