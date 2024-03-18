# microbit-module:Radio Communications Made By Cohen & Akshay@1.0

# to use this in microbit,download this file, click open in microbit, then click this file, then in your main type 'From radioComms import *' then 
# in a new line type run(to transmit type 'T' to boost type 'B' to receive type 'R', left motor spd, right motor spd)
from cyberbot import *
from microbit import *
import radio

maxSpeed = 100
fL, fR = 0, 0

# Functions to return status of left & right whiskkers. Inverts signal to make more clear.
def LW():
    if bot(15).read_digital() == 0:
        return False
    else:
        return True

def RW():
    if bot(0).read_digital() == 0:
        return False
    else:
        return True



# Will run left motor back if LW is true. Will run right motor back if RW is true.
def WRETURN():
    stop()
    L = 0
    R = 0
    
    if LW() == True:
        L = -1
    if RW() == True:
        R = -1
    if L != 0 or R != 0:
        display.show("W")
        bot(18, 19).servo_speed(L*fL,R*fR)
        sleep(500)
        stop()
        display.clear()
        return True

# Stops motors if either whisker is touched
def WSTOP():
        touched = False
        if LW() == 1:
            bot(18, 19).servo_speed(0,0)
            touched = True
        if RW() == 1:
            bot(18, 19).servo_speed(0,0)
            touched = True
        return touched

# Play sound and display to confirm robot is on
display.show(Image.SMILE)
audio.play(audio.SoundEffect(400, 800, 200, vol_end=255))
bot(22).tone(400, 100)
bot(22).tone(800, 100)
display.clear()

# Adjust speeds to allow easy setting of max speed
def movementSpeeds(lspd, rspd):
    global fL, fR
    
    leftRatio = 1
    leftReverse = False
    rightRatio = 1
    rightReverse = False

    if lspd < 0 or lspd == -0:
        leftReverse = True

    if rspd < 0 or rspd == -0:
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
    bot(18, 19).servo_speed(0,0)

# transmit values based on input
def transmit():
    while True:
        forward = 6
        back = 10
        left = 0
        right = 15
        # Buffer is how many times the radio signal will be sent when a button is pressed
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
            sleep(50)

        
            if direction == "B":
                display.show("B")
                move("B")
                WRETURN()
        

            elif direction == "L":
                display.show("L")
                move("L")
                WRETURN()
                
    
            elif direction == "R":
                display.show("R")
                move("R")
                WRETURN()
    

            elif direction == "F":
                display.show("F")
                move("F")
                WRETURN()
    
            else:
                stop()
                display.clear()
                WRETURN()

 
            
    
    while True:
        direction = str(radio.receive())
        start(direction)


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
        
