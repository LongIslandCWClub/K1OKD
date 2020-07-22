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

# Sox utility reference:
# http://linguistics.berkeley.edu/plab/guestwiki/index.php?title=Sox_in_phonetic_research

# function to generate band limited noise
function add_QRN {
    echo "making QRN for file $1"
    len=$(soxi -D $1)
    sox -r11025 -n noise.mp3 synth $len whitenoise vol 0.03 bandpass -c 650 500
    sox -m $1 noise.mp3 $2 
    rm noise.mp3
}

# Convert first message with QSB
ebook2cw -f 331 -w 24 -e 18 -p $1.txt
sox Chapter0000.mp3 $1.mp3  vol 0.75 

# Convert second message with no QSB
ebook2cw -f 653 -w 18 -e 18 -p $2.txt
sox Chapter0000.mp3 $2.mp3 vol 1.0 

# Convert third message with QSB
ebook2cw -f 1301 -w 25 -e 21 -p $3.txt
sox Chapter0000.mp3 $3.mp3 vol 0.5

# Combine all three files
sox -m $1.mp3 $2.mp3 $3.mp3 qrm.mp3 norm
rm Chapter0000.mp3 

# Generate band limited noise
add_QRN qrm.mp3 $4.mp3 gain -n -B 
sox $4.mp3 -n spectrogram -o $4.png
rm $1.mp3 $2.mp3 $3.mp3
rm qrm.mp3

open $4.png

