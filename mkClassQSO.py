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

# Default call and name for practice 
theirCall='W2LCW'
theirName='HOWARD'

# Personal information for QSO (change as needed)
myName='JERRY'
myCall='K1OKD'
myQTH='BOSTON, MA'
myRig='KX3'

def set_globals(call, name):
    global theirCall
    global theirName
    theirCall = call.upper() 
    theirName = name.upper() 

def mk_cq(direction):
    if direction == "call":
        print("CQ CQ DE", myCall, myCall, "K")
    else:
        print(theirCall, "DE", myCall, myCall, "K")

def mk_stage1(direction):
    if direction == "call":
        print(theirCall, "DE", myCall, end='')
        print(" TNX FER CALL <BT>", end='')
        print(" UR RST 5NN 5NN <BK>")
    else:
        print("<BK> RR TNX FER RPRT <BT>", end='')
        print(" UR RST 5NN 5NN <BK>")

def mk_stage2(direction):
    print("<BK> RR QTH IS", myQTH, myQTH, "<BK>")

def mk_stage3(direction):
    if direction == "call":
        print("<BK> RR MY NAME IS", myName, myName, "<BK>")
    else:
        print("<BK> RR", theirName, "MY NAME IS", myName, myName, "<BK>")

def mk_stage4(direction):
    if direction == "call":
        print("<BK> RR", theirName, "TNX FER QSO ES 73 ", end='')
        print(theirCall, "DE", myCall, "<SK>")
    else:
        print(theirCall, "DE", myCall, "TU ES 73 <SK> <DIT> <DIT>")

if __name__ == "__main__":
    set_globals(sys.argv[1], sys.argv[2])
    direction=sys.argv[3].lower()
    print("")
    mk_cq(direction)
    mk_stage1(direction)
    mk_stage2(direction)
    mk_stage3(direction)
    mk_stage4(direction)
    print("")
       
