from cyberbot import *
from microbit import *
from time import *

freqA = 60_000
freqB = 50_000
freq = 0
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
            freq = 0
            display.clear()
    
        if freq != 0:
            sleep = (us_s / freq) / 2
            
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

        if A == 0:
            display.show("A")
            sleep_ms(20)
            
        elif B == 0:
            display.show("B")
            sleep_ms(20)
        else:
            display.clear()

def run(type):
    if type == "T":
        transmit()
    if type == "R":
        transmit()
