# microbit-module:Radio Communications Made By Cohen & Akshay@1.0

# to use this in microbit,download this file, click open in microbit, then click this file, then in your main type 'From radioComms import *' then 
# in a new line type run(to transmit type 'T' to boost type 'B' to receive type 'R', left motor spd, right motor spd)
from cyberbot import *
from microbit import *
import music
import radio


LW = 15
RW = 0

# turn on sound
bot(22).tone(400, 10)
bot(22).tone(800, 10)

# stop motors
def stop():
    bot(18).servo_speed(None)
    bot(19).servo_speed(None)


def WSTOP():
        touched = False
        if LW == 1:
            bot(18).servo_speed(None)
            touched = True
        if RW == 1:
            bot(19).servo_speed(None)
            touched = True

        return touched

def WRETURN(lspd, rspd):
        touched = False
        if LW == 1 or RW == 1:
            bot(18).servo_speed(-lspd)
            bot(19).servo_speed(-rspd)
            sleep(1000)
            stop()
        return touched



# move motors accordingly, if no wait keep moving
def move(lspd,rspd,wait):


    bot(18).servo_speed(lspd)
    bot(19).servo_speed(rspd)

    if wait != 0:
            sleep(wait)
            stop()


        





# transmit values based on input
def transmit():
    while True:
        forward = 6
        back = 10
        left = 0
        right = 15
        buffer =1

        
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
def receive(left,right):
    def start(direction):

            if direction == "B":
                display.show('B')
                move(-left,-right,0)

            elif direction == "L":
                display.show('L')
                move(-left,right,0)
    
            elif direction == "R":
                display.show('R')
                move(left,-right,0)
        
            elif WRETURN(left, right) == True:
                print()

            elif direction == "F":
                display.show('F')
                move(left,right,0)
    
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
    leftspeed = leftMoveSpd
    rightspeed = rightMoveSpd
    
    radio.config(group=10)
    # for any configs


    # transmit
    if trs == "T":
        transmit()

    # recive
    elif trs == "R":
        
        receive(leftspeed,rightspeed)

    # boost
    elif trs == "B":
        booster()

    # error
    else:
        display.show('ERROR')
        
