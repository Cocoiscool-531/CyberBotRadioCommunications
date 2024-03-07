# microbit-module:Radio Communications Made By Cohen & Akshay@0.0.5
from cyberbot import * 
from microbit import *
import radio

leftSpeed = -74.25
rightSpeed = 75


# Receive Code


def receive():
    
    # Movement Code
    
    def move(a):
        if a == "L":
            display.show("L")
            bot(18).servo_speed(-leftSpeed)
            bot(19).servo_speed(leftSpeed)
            
        elif a == "F":
            display.show("F")
            bot(18).servo_speed(leftSpeed)
            bot(19).servo_speed(leftSpeed)

        elif a == "B":
            display.show("B")
            bot(18).servo_speed(-leftSpeed)
            bot(19).servo_speed(-leftSpeed)

        elif a == "R":
            display.show("R")
            bot(18).servo_speed(leftSpeed)
            bot(19).servo_speed(-leftSpeed)

        elif a == "S":
            display.clear()
            bot(18).servo_speed(None)
            bot(19).servo_speed(None)

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
        radio.send_bytes(b'00')

    elif forward == True:
        display.show("F")
        radio.send_bytes(b'01')

    elif backward == True:
        display.show("B")
        radio.send_bytes(b'10')

    elif rightTurn == True:
        display.show("R")
        radio.send_bytes(b'11')

    else:
        display.clear()

# Main Run Loop, Pass in "B" for both, "T" for transmit, and "R" for reciever
def run(s):
    display.on()
    speaker.on()
    radio.on()
    radio.config(data_rate=radio.RATE_2MBIT)

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
