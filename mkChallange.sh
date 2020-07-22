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
 
say -r200  $(echo "the phrase,, " && cat $1.txt | tr -d = && \
    echo ",, played at 21 18, 20 15, 18 13, and 15 10 WPM") -o $1
ebook2cw -f 650 -w 21 -e 18 -p $1.txt
mv Chapter0000.mp3 tmp0.mp3
ebook2cw -f 650 -w 20 -e 15 -p $1.txt
mv Chapter0000.mp3 tmp1.mp3
ebook2cw -f 650 -w 18 -e 13 -p $1.txt
mv Chapter0000.mp3 tmp2.mp3
ebook2cw -f 650 -w 15 -e 10 -p $1.txt
mv Chapter0000.mp3 tmp3.mp3
rm $1.mp3
mp3cat tmp0.mp3 tmp1.mp3 tmp2.mp3 tmp3.mp3  -o $1.mp3
rm tmp?.mp3

#$1.mp3 

