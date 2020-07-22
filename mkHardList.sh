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
 
cat << PYTHON_SCRIPT > mkHard.py
#!/usr/bin/env python 
import random
import sys

def mk_list(length):
    ''' make hard list '''
    hard_list = ['B', 'D', 'S', 'H', 'U', 'V',]
    char_list = ['A', 'C', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', \
                      'P', 'Q', 'R', 'T', 'W', 'X', 'Y', 'Z', '1', '2', '3', \
                      '4', '5', '6', '7', '8', '9', '0', ',', '?', '.', '/', \
                      '<BT>', '<SK>', '<KN>', '<AR>', '<BK>']
    print("vvv vvv")
    print(" ")
    for i in range(1, length):
        char = random.choice(char_list)
        print(char, end='')
        char = random.choice(hard_list)
        print(char, end='')
        char = random.choice(char_list)
        print(char, end='')
        char = random.choice(hard_list)
        print(char, end='')
        char = random.choice(char_list)
        print(char, end='')
        print(" ")
        if i % 5 == 0: 
            print(" ")
    print(" ")

if __name__ == "__main__":
    length = 26
    if len(sys.argv) > 1:
        length = int(sys.argv[1])+1
    mk_list(length)
PYTHON_SCRIPT
chmod +x mkHard.py

./mkHard.py $1 > hard_tmp.txt
ebook2cw -f 650 -w 25 -e 20 -p hard_tmp.txt 
cat hard_tmp.txt && play Chapter0000.mp3
rm mkHard.py hard_tmp.txt Chapter0000.mp3

