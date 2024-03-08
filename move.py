#microbt-module: mov @2.0
from cyberbot import *
from microbit import *
import music
import radio



# turn on sound
music.pitch(185,1000)




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
    forward = 2
    back = 13
    left = 0
    right = 15
    
    if bot(forward) == 1:
        display.show('F')
        for i in range(5):

            radio.send("F")
        
    if bot(back) == 1:
        display.show('B')
        for i in range(5):
            radio.send("B")
        
    if bot(left) == 1:
        display.show('C')
        for i in range(5):
            radio.send("L")
        
    if bot(right) == 1:
        display.show('D')
        for i in range(5):
            radio.send("R")

    # to stop over flooding
    sleep(50)
            



# recive inputs and move
def receive(left,right):
    while True:



    
        def start(direction):

            
            if direction == "F":
                display.show('F')
                move(left,right,0)
                
            if direction == "B":
                display.show('B')
                move(-left,-right,0)
                
            if direction == "L":
                display.show('L')
                move(left,-right,0)
    
            if direction == "R":
                display.show('R')
                move(left,right,0)
    
            else:
                stop()
                
        direction = str(radio.receive())
        start(direction)
        sleep(50)
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
        
