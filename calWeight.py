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
import sys

def calc_weight(in_string, CWPM, FWPM):
    ''' calculate weight and speed '''
    weight_dict = {'A' :  5, 'B' :  9, 'C' : 11, 'D' :  7, 'E' :  1, \
                   'F' :  9, 'G' :  9, 'H' :  7, 'I' :  3, 'J' :  9, \
                   'K' :  9, 'L' :  9, 'M' :  7, 'N' :  5, 'O' : 11, \
                   'P' : 11, 'Q' : 13, 'R' :  7, 'S' :  5, 'T' :  3, \
                   'U' :  7, 'V' :  9, 'W' :  9, 'X' : 11, 'Y' : 13, \
                   'Z' : 11, '1' : 17, '2' : 15, '3' : 13, '4' : 11, \
                   '5' :  9, '6' : 11, '7' : 13, '8' : 15, '9' : 17, \
                   '0' : 19, ',' : 19, '?' : 15, '.' : 17, '/' : 13}

    num_spaces = len([s for s in in_string if s == ' '])
    char_list = [s.upper() for s in in_string if s != ' ']
    weight_list = [weight_dict[s] for s in char_list]
    weight = sum(weight_list) + 3 * (len(char_list)-1) + 7 * num_spaces
    send_time = (1.2/CWPM) * sum(weight_list)        \
              + (1.2/FWPM) * 3.0 *(len(char_list)-1) \
              + (1.2/FWPM) * 7.0 * num_spaces
    send_time = round(send_time, 1)

    print(" input: '", in_string, "'", sep='')
    #print("number of spaces: ", num_spaces)
    #print("number of characers: ", len(char_list))
    #print("string to calc: ", char_list)
    #print("weight list: ", weight_list)
    if CWPM == FWPM:
        print(" speed:", CWPM, "WPM")
    else: 
        print(" speed:", CWPM, "WMP with Farnsworth of", FWPM, "WPM")
    print("weight:", weight)
    print("  time:", send_time, "seconds")
    print(" ")

if __name__ == "__main__":
    # ./calWeight.py 25 25 "$(< input.txt)"
    CWPM = float(sys.argv[1])
    FWPM = float(sys.argv[2])
    in_text = ''.join(sys.argv[3:len(sys.argv)])
    calc_weight(in_text, CWPM, FWPM)
