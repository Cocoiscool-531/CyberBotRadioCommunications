from cyberbot import *
from microbit import *
from time import *
from tv_remote import *
import machine

freqA = 60_000
freqB = 50_000
freq = 0
sleep = 0
us_s = 1000000

header = 2400
oneBit = 12000
zeroBit = 600
pause = 600

def on():
    bot(0).write_digital(1)
def off():
    bot(0).write_digital(0)


def send(_1, _2, _3, _4, _5, _6, _7, _8=1, _9=0, _10=0, _11=0,_12=0):
    for i in range(1, 12):
        if eval("_"+str(i)) == 1:
            eval("_"+str(i)+" = oneBit")
        else:
            eval("_"+str(i)+" = zeroBit")

    on()
    sleep_us(header)
    off()
    for i in range(1, 12):
        sleep_us(pause)
        on()
        sleep_us(eval("_"+str(i)))
        off()

def transmit():
    while True:
        A = button_a.is_pressed()
        B = button_b.is_pressed()
    
        if A:
            send(0,0,0,0,0,0,0)
        elif B:
            send(1,0,0,0,0,0,0)
        sleep_ms(45)

def recieve():
    while True:
        n = ir(0).remote()
        if n == 0:
            display.show("0")
        elif n == 1:
            display.show("1")
        else:
            display.clear()

def run(type):
    if type == "T":
        transmit()
    if type == "R":
        recieve()
