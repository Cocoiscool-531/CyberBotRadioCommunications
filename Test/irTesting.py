from cyberbot import *
from microbit import *
from time import *
from tv_remote import *
header = 2400
oneBit = 12000
zeroBit = 600
pause = 600

def on():
    bot(0).write_digital(1)
def off():
    bot(0).write_digital(0)


def send(command=[], device=[0,0,0,0,1]):
    full=[]
    command.reverse()
    device.reverse()
    for i in range(1, 12):
        if full[i] == 1:
            full[i] = oneBit
        else:
            full[i] = zeroBit

    on()
    sleep_us(header)
    off()
    
    for i in range(1, 12):
        sleep_us(pause)
        on()
        sleep_us(full[i])
        off()

def transmit():
    while True:
        A = button_a.is_pressed()
        B = button_b.is_pressed()
    
        if A:
            send(CommandCodes.key1)
        elif B:
            send(CommandCodes.key2)
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

class CommandCodes():
    key1        = [0,0,0,0,0,0,0]
    key2        = [0,0,0,0,0,1,0]
    key3        = [0,0,0,0,0,1,1]
    key4        = [0,0,0,0,1,0,0]
    key5        = [0,0,0,0,1,0,1]
    key6        = [0,0,0,0,1,1,0]
    key7        = [0,0,0,0,1,1,1]
    key8        = [0,0,0,1,0,0,0]
    key9        = [0,0,0,1,0,0,1]
    key0        = [0,0,0,1,0,1,0]
    channelPlus = [0,0,1,0,0,0,0]
    channelMinu = [0,0,1,0,0,0,1]
    volumePlus  = [0,0,1,0,0,1,0]
    volumeMinu  = [0,0,1,0,0,1,1]
    mute        = [0,0,1,0,1,0,0]
    power       = [0,0,1,0,1,0,1]
    enter       = [0,0,0,1,0,1,1]
    input       = [0,1,0,0,1,0,1]
    up          = [1,1,1,0,1,0,0]
    down        = [1,1,1,0,1,0,1]
    left        = [0,1,1,0,0,1,1]
    right       = [0,1,1,0,1,0,0]
