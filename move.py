# Imports go at the top
from cyberbot import *
from microbit import *
import radio
radio.on()

display.on()
vals = ["A","B"]
buffer = 1000


def move(lspd,rspd,wait):
    bot(18).servo_speed(lspd)
    bot(19).servo_speed(rspd)
    #sleep(wait)
    #stop()


def stop():
    bot(18).servo_speed(0)
    bot(19).servo_speed(0)












# main loop
while True:
    # recive code


    # recive A
    # go left
    if radio.receive_bytes() == b'00':
        display.show("L")
        move(-74.25,-75,3000)




    

    # recive C
    # go back
    elif radio.receive_bytes() == b'01':
        display.show("B")
        move(-74.25,75,3000)






    


    # recive B
    # go forward
    elif radio.receive_bytes() == b'10':
        display.show("F")
        move(74.25,-75,3000)

    


    

    # recive D
    # go right
    elif radio.receive_bytes() == b'11':
        display.show("R")
        move(74.25,75,3000)



    


    
    # stop
    else:
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
        display.clear()

    if button_a.is_pressed() and button_b.is_pressed():
        stop()
        display.clear()


