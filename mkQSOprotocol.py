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

# Random selection of call sign (add as needed)
theirCall='W2LCW'
call_list = ['VK5PL', 'W5NWT', 'W5BHR', 'N1RBD', 'W5DMD', 'KE0YMM', 'WX8YZ', \
             'KF0W', 'W8KO', 'KF5INS', 'VE2GTZ', 'K3ARC', 'W7JMM', 'AC2KZ', \
             'K6ZX', 'NV1U', 'NV9P', 'K2RBL', 'W7JNM', 'K1SAC', 'VA2YAF', \
             'W0TS', 'WB5MET', 'AA6MK', 'KI7EIH', 'NQ8T', 'WB8AM', 'VA2SOB', \
             'AG7YY', 'WX9U', 'G4XWJ', 'KE8KOR', 'AA0Z', 'KG6T', 'N1CC', \
             'K1HOM', 'WU3K', 'NO7E', 'KN4UDT', 'KD6GBY', 'KH7LM', 'WA4GSD', \
             'K1FA', 'KE8MCR', 'W4KTX', 'WJ0B', 'KD8GH', 'N3XPD', 'WB2GXM', \
             'W2ITT', 'K2MZ', 'KE0VRH', 'K4IGL', 'N5SEZ', 'K0ES', 'N8KDC', \
             'AC2LI', 'W2KFV', 'KC2KC', 'W2OSR', 'KD9FPC', 'AG5AT', 'K1CRG', \
             'AG7FH', 'N1EYO', 'W9BJA', 'KB2RSQ', 'KC1TN', 'F5JYA', 'W3TBC', \
             'K6PDL', 'W3SLH', 'K4RLC', 'KD2SPJ', 'KB5HSC', 'K8BMA', 'WK4T', \
             'E25JRP', 'KF5DNI', 'WA5CXG', 'K4GSW', 'W0JCB', 'WS4K', 'K5UTM', \
             'KM4OPN', 'W7SKH', 'W7CRB', 'K8TAF', 'W7PAT', 'AJ6CQ', 'KG7EMV', \
             'KG6EYE' ]

# Random selection of operator name (add as needed)
theirName='HOWARD'
name_list = [ 'ARTHUR', 'AUG', 'BEV', 'BOB', 'BRAD', 'BRIAN', 'BRUCE', \
            'BRYAN', 'CARLOS', 'CASEY', 'CHARLES', 'CHRIS', 'CHUCK', 'CLAUDE', \
            'COURTNEY', 'DAN', 'DAVE', 'DAVID', 'DENNIS', 'DOUG', 'ERIC', \
            'EVANS', 'GARR', 'GARY', 'GENE', 'HARRY', 'HERB', 'HERMAN', \
            'HOWARD', 'JERRY', 'JIM', 'JIMMY', 'JOE', 'JOHN', 'KEN', 'KEVIN', \
            'KYLE', 'MARINO', 'MARK', 'MICHAEL', 'MIKE', 'MIRON', 'PAT', \
            'PAUL', 'PETE', 'RAMON', 'RANDY', 'RAY', 'RICH', 'RICHARD', \
            'RICK', 'ROB', 'ROBB', 'SAM', 'SEBASTIEN', 'SIDNEY', 'SLEIGH', \
            'STEPHEN', 'STEVE', 'SUE', 'SUPOJ', 'TJ', 'TIM', 'TOM', 'WAYN', \
            'WILL', 'WILLIAM', 'YANICK' ] 

# Personal information for QSO (change as needed)
myName='JERRY'
myCall='K1OKD'
myQTH='BOSTON, MA'
myRig='KX3'
myMaxPower='110'
myAnt='DIPOLE'
myAntHeight='32'
myAge='55'
myJob='SOFTWARE ENGINEER'
myOtherHobby='FLY FISHING ES HARLEY RIDING'
myYrsAham='3'

def set_globals():
    global theirCall
    global theirName
    theirCall = random.choice(call_list)
    theirName = random.choice(name_list)

def mk_cq():
    print("QRL? QRL?  ", end='')
    print("CQ CQ DE", myCall, myCall, "K")
    print('')

def mk_stage1():
    good_list = ['GM', 'GA', 'GE', 'GD' ]
    print(theirCall, "DE", myCall)
    print(random.choice(good_list), "ES TNX FER CALL <BT>")
    rst = random.choice(['2', '3', '4','5'])
    rst += random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    rst += random.choice(['7', '8', '9'])
    print("UR RST", rst, rst, end='')
    print(random.choice(['', ' WID QSB', ' WID QRM', ' WID QRN']), '<BT>')
    print("QTH NR", myQTH, myQTH, "<BT>")
    print("NAME", myName, myName, "<BT>")
    print("SO HW? <AR>", theirCall, "DE", myCall, "K")
    print('')

def mk_stage2():
    print(theirCall, "DE", myCall)
    print("RR SLD CPY", theirName, "ES TU FER RPRT <BT>")
    power = random.randint(1,int(myMaxPower))
    print("MY RIG", myRig, "AT", power, "WATTS", end='')
    if power <= 5:
        print(" QRP", end='')
    print(" <BT>")
    print("MY ANT", myAnt, "UP", myAntHeight, "FT <BT>")
    temp = random.randint(10,100)
    if temp < 30:
        wx = random.choice(['SUNNY', 'SUN', 'BREEZY', 'CLOUDY', 'CLOUDS', 
            'CLEAR', 'COLD', 'ICE', 'SNOW', 'SLEET'])
    elif temp > 85: 
        wx = random.choice(['SUNNY', 'SUN', 'BREEZY', 'CLOUDY', 'CLOUDS', 
            'CLEAR', 'STORMS', 'HUMID', 'HOT'])
    else:
        wx = random.choice(['SUNNY', 'SUN', 'BREEZY', 'CLOUDY', 'CLOUDS', 
            'CLEAR', 'RAIN', 'COOL'])
    print("WX HR", wx, "ES TEMP", temp, "DF <BT>")
    print("OK HW? <AR>", theirCall, "DE", myCall, "K")
    print('')

def mk_stage3():
    print(theirCall, "DE", myCall)
    print("RR FB", theirName, "ES TU FER INFO <BT>")
    print("BEEN A HAM FER", myYrsAham, "YRS <BT>")
    print("MY JOB IS", myJob, "<BT>")
    print("OTHER HOBBY", myOtherHobby, "<BT>")
    print("MY AGE", myAge, "YRS <BT>")
    print("HW NOW? <AR>", theirCall, "DE", myCall, "K")
    print('')

def mk_stage4():
    print(theirCall, "DE", myCall)
    qrt = random.choice(['A SCHED', 'BED', 'DINNER', 'WORK', 'A NET', \
            'SCHOOL', 'A MEETING', 'MY XYL'])
    print("OK", theirName, "MUST QRT NOW FER", qrt, "<BT>")
    print("TU FER NICE QSO, HPE CUAGN <BT>")
    print("73 <AR>", theirCall, "DE", myCall, "<SK>")
    print('')

if __name__ == "__main__":
    set_globals()
    mk_cq()
    mk_stage1()
    mk_stage2()
    mk_stage3()
    mk_stage4()
        
