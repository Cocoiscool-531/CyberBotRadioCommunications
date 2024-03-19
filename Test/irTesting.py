# Imports go at the top
from microbit import *
from cyberbot import *

freq = 37500
lastPrinted = ""

while True:
    iRr = bot(1, 2).ir_detect(37500)
    iRl = bot(14, 13).ir_detect(37500)

    if iRl == 0 and iRr == 0:
        bot(22).tone(200, 100)
        display.show("B")
    elif iRl == 0:
        bot(22).tone(600, 100)
        display.show("L")
    elif iRr == 0:
        bot(22).tone(1000, 100)
        display.show("R")
    else:
        bot(22).tone(0, 0)
        display.clear()
