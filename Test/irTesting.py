from cyberbot import *
from microbit import *
from time import *

freqA = 15_000
freqB = 20_000
freq = 1
sleep = 0
us_s = 1000000

def transmit():
    while True:
        if button_a.is_pressed():
            freq = freqA
            display.show("A")
        elif button_b.is_pressed():
            freq = freqB
            display.show("B")
        else:
            freq = 1
            display.clear()

        sleep = us_s / freq
    
        if freq != 1:
            sleep_us(int(sleep))
            bot(5).write_digital(1)
            bot(0).write_digital(1)
            sleep_us(int(sleep))
            bot(5).write_digital(0)
            bot(0).write_digital(0)
        else:
            bot(0).write_digital(0)
            bot(5).write_digital(0)

def recieve():
    while True:
        A = bot(15, 0).ir_detect(freqA)
        B = bot(15, 0).ir_detect(freqB)

        if A == 1:
            display.show("A")
        elif B == 1:
            display.show("B")
        else:
            display.clear()

def run(type):
    if type == "T":
        transmit()
    if type == "R":
        transmit()
