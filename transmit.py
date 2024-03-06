# Imports go at the top
from cyberbot import *
from microbit import *
import radio
radio.on()
speaker.on()
display.on()

forward = False
backward = False
leftTurn = False
rightTurn = False


while True:
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
