# microbit-module:Radio Communications Made By Cohen & Akshay@1.0

# to use this in microbit,download this file, click open in microbit, then click this file, then in your main type 'From radioComms import *' then 
# in a new line type run(to transmit type 'T' to boost type 'B' to receive type 'R', left motor spd, right motor spd)
from cyberbot import *
from microbit import *
import radio

maxSpeed = 100
fL, fR = 0, 0

# left and right whikers
LW = 15
RW = 0



def WBIND():
    NR = []
    if bot(LW).read_digital() == 1:
            bot(18).servo_speed(None)
            NR.append("L")
            
            
    if RW == 1:
            bot(19).servo_speed(None)
            NR.append("R")
            
    if LW and RW == 1:
            NR.append("F")
    return NR
    



# turn on sound
bot(22).tone(400, 10)
bot(22).tone(800, 10)

def movementSpeeds(lspd, rspd):
    global fL, fR
    
    leftRatio = 1
    leftReverse = False
    rightRatio = 1
    rightReverse = False

    if lspd < 0:
        leftReverse = True

    if rspd < 0:
        rightReverse = True
    
    if lspd > rspd: 
        rightRatio = rspd / lspd
    elif rspd > lspd: 
        leftRatio = lspd / rspd
    
    if lspd > maxSpeed:
        lspd = maxSpeed
    if rspd > maxSpeed:
        rspd = maxSpeed
    
    fL = lspd * leftRatio
    fR = rspd * rightRatio

    if leftReverse == True:
        fL = -fL
    if rightReverse == True:
        fR = -fR

# move motors accordingly, if no wait keep moving
def move(type, wait=0):

    if type == "L":
        bot(18,19).servo_speed(-fL,fR)

    if type == "F":
        bot(18,19).servo_speed(fL,fR)

    if type == "B":
        bot(18,19).servo_speed(-fL,-fR)

    if type == "R":
        bot(18,19).servo_speed(fL,-fR)

    if wait != 0:
            sleep(wait)
            stop()

# stop motors
def stop():
    bot(18, 19).servo_speed()


def WSTOP():
        touched = False
        if LW == 1:
            bot(18, 19).servo_speed()
            touched = True
        if RW == 1:
            bot(18, 19).servo_speed()
            touched = True
        return touched

def WRETURN():
        touched = False
        if LW == 1 or RW == 1:
            touched = True
            move("R")
            sleep(1000)
            stop()
            return touched

# transmit values based on input
def transmit():
    while True:
        forward = 6
        back = 10
        left = 0
        right = 15
        buffer = 1

        
        if bot(forward).read_digital() == 1:
            for i in range(buffer):
                radio.send("F")
            display.show("F")
            
        elif bot(back).read_digital() == 1:
            for i in range(buffer):
                radio.send("B")
            display.show("B")
            
        elif bot(left).read_digital() == 1:
            for i in range(buffer):
                radio.send("L")
            display.show("L")
            
        elif bot(right).read_digital() == 1:
            for i in range(buffer):
                radio.send("R")
            display.show("R")
    
        else:
            display.clear()

        sleep(50)
            



# recive inputs and move
def receive():
    def start(direction):

            if direction == "B":
                display.show("B")
                move("B")

            elif direction == "L":
                display.show("L")
                move("L")
    
            elif direction == "R":
                display.show("R")
                move("R")
        
            elif WRETURN() == True:
                print()

            elif direction == "F":
                display.show("F")
                move("F")
    
            else:
                stop()
                display.clear()

 
            
    
    while True:
        direction = str(radio.receive())
        start(direction)
        # delay to reduce noise






# boost the signal for long distance
def booster():
    while True:
        radio.send(str(radio.receive()))
        sleep(50)
    





# base code to run trasmit, booster and recive code
def run(trs,leftMoveSpd,rightMoveSpd):
    import radio
    radio.on()
    # our bot uses 75,75
    if leftMoveSpd == 0:
        leftMoveSpd = 9999
    if rightMoveSpd == 0:
        leftMoveSpd = 9999

    movementSpeeds(leftMoveSpd, rightMoveSpd)
    
    radio.config(group=10)
    # for any configs

    # transmit
    if trs == "T":
        transmit()

    # recive
    elif trs == "R":
        
        receive()

    # boost
    elif trs == "B":
        booster()

    # error
    else:
        display.show('ERROR')
        
