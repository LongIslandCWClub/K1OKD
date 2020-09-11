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

import sys

def fixup_file(in_file, out_file):
    ''' remove and/or replace unwanted characters from text file '''
    # character mapping dictionary 
    map_chars = { 
            '~' : '',
            '`' : '',
            '’' : '',
            '‘' : '',
            '!' : '.',
            '#' : 'No. ',
            '$' : '',
            '%' : '',
            '^' : '',
            '&' : '',
            '*' : '',
            '@' : '',
            '(' : '',
            ')' : '',
            '-' : ' ',
            '_' : ' ',
            '|' : '',
            '+' : '',
            '=' : '',
            '[' : '',
            ']' : '',
            '{' : '',
            '}' : '',
            '>' : '',
            '<' : '',
            '"' : '',
            '“' : '',
            '”' : '',
            ';' : ',',
            ':' : ',',
            '—' : ',', 
            '\'' : '',
            '\\' : '/',
            '\t' : '    ',
            '\n' : ' '
            }

    # read input file
    inFile = open(in_file, 'r')
    inLines = inFile.readlines()
    inFile.close()

    # replace mapped characters
    outLines = []
    for line in inLines: 
        # add spaces and paragraph separator for blank lines
        if line == "\n":
            line = "<BT> \n"
        else:
            for char in map_chars:
                line = str(line).replace(char, map_chars[char]).upper()
        outLines.append(line)
    
    # write output file
    outFile = open(out_file, 'w')
    outFile.writelines(outLines)
    outFile.close()

if __name__ == "__main__":
    # first argument is input file, 2nd argument is output file
    in_file = str(sys.argv[1])
    out_file = str(sys.argv[2])
    fixup_file(in_file, out_file)

