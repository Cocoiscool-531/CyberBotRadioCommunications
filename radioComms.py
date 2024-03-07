# microbit-module:Radio Communications Made By Cohen & Akshay@0.0.5
from cyberbot import * 
from microbit import *
import radio

leftSpeed = 67
rightSpeed = -75

# prep-programed code

def prepro1():
    # nothing
    print("null")



def prepro2():
    # nothing
    print("null")

def stop():
    bot(18).servo_speed(0)
    bot(19).servo_speed(0)



def moveMotor(lspd,Rspd,wait):
    bot(18).servo_speed(lspd)
    bot(19).servo_speed(Rspd)
    sleep(wait)
    stop()
    
    




# Receive Code


def receive():
    
    # Movement Code
    
    def move(a):
        if a == "L":
            display.show("L")
            moveMotor(leftSpeed,rightSpeed,0)

            
        elif a == "F":
            display.show("F")
            moveMotor(leftSpeed,-rightSpeed,0)


        elif a == "B":
            display.show("B")
            moveMotor(-leftSpeed,rightSpeed,0)


        elif a == "R":
            display.show("R")
            moveMotor(leftSpeed,-rightSpeed,0)


        elif a == "S":
            display.clear()
            stop()

    # Scan for radio signals and move accordingly

    #↓ Transmitted as 1 bit, doesn't take long ↓
    if radio.receive_bytes() == b'00':
        move("L")

    elif radio.receive_bytes() == b'01':
        move("F")
    #↑ Transmitted as 1 bit, doesn't take long ↑

    #↓ Transmitted as 2 bits, takes long ↓
    elif radio.receive_bytes() == b'10':
        move("B")

    elif radio.receive_bytes() == b'11':
        move("R")
    #↑ Transmitted as 2 bits, takes long ↑

    else:
        move("S")

    




# Transmitting Code


def transmit():
    forward = False
    backward = False
    leftTurn = False
    rightTurn = False

    # Read Buttons Pressed Value
    if  bot(0).read_digital() == 1:
        leftTurn = True
    else:
        leftTurn = False

    if  bot(2).read_digital() == 1:
        forward = True
    else:
        forward = False

    if  bot(13).read_digital() == 1:
        backward = True
    else:
        backward = False

    if  bot(15).read_digital() == 1:
        rightTurn = True
    else:
        rightTurn = False

    # Act Based On Button Values
    
    if leftTurn == True:
        display.show("L")
        radio.send("L")

    elif forward == True:
        display.show("F")
        radio.send("F")

    elif backward == True:
        display.show("B")
        radio.send("B")

    elif rightTurn == True:
        display.show("R")
        radio.send("R")

    else:
        display.clear()
# Main Run Loop, Pass in "B" for both, "T" for transmit, and "R" for reciever
def run(s):
    display.on()
    speaker.on()
    radio.on()
    radio.config(power=5, data_rate=radio.RATE_2MBIT, channel=42)

    bot(22).tone(500, 1000)
    
    if s == "B":
        while True:
            receive()
            transmit()

    elif s == "R":
        while True:
            receive()

    elif s == "T":
        while True:
            transmit()
