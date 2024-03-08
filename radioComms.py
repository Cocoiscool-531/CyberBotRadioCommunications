# microbit-module:Radio Communications Made By Cohen & Akshay@0.5
from cyberbot import *
from microbit import *
import music
import radio


# turn on sound
music.pitch(185,1000)
bot(22).tone(400, 100)
bot(22).tone(800, 100)

# stop motors
def stop():
    bot(18).servo_speed(None)
    bot(19).servo_speed(None)





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
        forward = 2
        back = 13
        left = 0
        right = 15
        
        if bot(forward).read_digital() == 1:
            for i in range(5):
                radio.send("F")
                display.show("F")
            
        elif bot(back).read_digital() == 1:
            for i in range(5):
                radio.send("B")
                display.show("B")
            
        elif bot(left).read_digital() == 1:
            for i in range(5):
                radio.send("L")
                display.show("L")
            
        elif bot(right).read_digital() == 1:
            for i in range(5):
                radio.send("R")
                display.show("R")
    
        else:
            display.clear()
    
        # to stop over flooding
        sleep(100)
            



# recive inputs and move
def receive(left,right):
    def start(direction):

            if direction == "F":
                display.show('F')
                move(left,right,0)
                
            if direction == "B":
                display.show('B')
                move(-left,-right,0)
                
            if direction == "L":
                display.show('L')
                move(-left,right,0)
    
            if direction == "R":
                display.show('R')
                move(left,-right,0)
    
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
def run(trs,leftMoveSpd=75.0,rightMoveSpd=75.0):
    import radio
    radio.on()
    
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
        
