#!/usr/bin/env python 

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

import random

def mk_list():
    ''' make random list '''
    character_list = ['A', 'B', 'C', 'D', 'E', \
                      'F', 'G', 'H', 'I', 'J', \
                      'K', 'L', 'M', 'N', 'O', \
                      'P', 'Q', 'R', 'S', 'T', \
                      'U', 'V', 'W', 'X', 'Y', \
                      'Z', '1', '2', '3', '4', \
                      '5', '6', '7', '8', '9', \
                      '0', ',', '?', '.', '/']

    print("vvv vvv ")
    for i in range(0, 8):
        for j in range(0, 5):
            char = random.choice(character_list)
            print(char, end='')
            character_list.remove(char)
        print(" ")
        if i == 3:
            print("+ = ")
    print("> bk ")
    print(" ")

if __name__ == "__main__":
    mk_list()
