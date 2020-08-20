#!/bin/bash

# Copyright (c) 2020 Jerry Doty (K1OKD)
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject
# to the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
# ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 cat << PYTHON_SCRIPT > inst_req.py
#!/usr/bin/env python 
import random
def mk_list():
    character_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '?', '.', '/', '<BT>', '<SK>', '<BK>', '<AR>', '<KN>']
    for i in range(0, len(character_list)):
        char = random.choice(character_list)
        print(char, " ", end='')
        character_list.remove(char)
if __name__ == "__main__":
    mk_list()
PYTHON_SCRIPT
chmod +x inst_req.py
chars=$(./inst_req.py)
rm inst_req.py

function map_char {
    local char=""
    case $1 in
        '?') char="question" ;;
        '/') char="stroke" ;;
        '.') char="period" ;;
        ',') char="comma" ;;
        '<AR>') char="AR" ;;
        '<BT>') char="BT" ;;
        '<BK>') char="BK" ;;
        '<SK>') char="SK" ;;
        '<KN>') char="KN" ;;
        '<AS>') char="AS" ;;
        *) char=$1 ;;
    esac
    echo $char 
}

wpm=25
if [ "$1" != "" ]; then
    wpm=$1
fi

delay=0.5
if [ "$2" != "" ]; then
    delay=$2
fi

out_file="instant_recognition"
if [ "$3" != "" ]; then
    out_file=$3
fi

echo -n "working on it... "
add_silence=0
if (( $(echo "$delay > 0.026" |bc -l) )); then
    dur=$(echo $delay - 0.026 | bc)
    sox -n -r 22050 -c 1 silence.mp3 trim 0.0 $dur > /dev/null 2>&1
    add_silence=1
fi 
for c in $chars; do
    echo $c | ebook2cw -s22050 -f 650 -w $wpm -p - > /dev/null 2>&1
    c=$(map_char $c)
    say -r200 -o sayit $(echo "$c") > /dev/null 2>&1
    sox sayit.aiff sayit.mp3 > /dev/null 2>&1
    if [ $add_silence -eq 1 ]; then
        sox Chapter0000.mp3 silence.mp3 sayit.mp3 silence.mp3 $c.mp3 norm > /dev/null 2>&1
    else
        sox Chapter0000.mp3 sayit.mp3 $c.mp3 norm > /dev/null 2>&1
    fi 
    rm Chapter0000.mp3 sayit.aiff sayit.mp3 
done
if [ $add_silance -eq 1 ]; then
    rm silence.mp3
fi

filse=""
for c in $chars; do
    c=$(map_char $c)
    file="$c.mp3 "
    files="$files$file"
done
sox $files "$out_file.mp3" > /dev/null 2>&1
rm $files
echo "Done!"
echo $chars

