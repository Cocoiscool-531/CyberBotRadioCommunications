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
    sleep(wait)
    bot(18).servo_speed(0)
    bot(19).servo_speed(0)


def stop():
    bot(18).servo_speed(0)
    bot(19).servo_speed(0)



while True:
    
    if button_a.is_pressed():
        audio.play(audio.SoundEffect())
        for i in range(buffer):
            radio.send('A')
            sleep(1)
        
    elif button_b.is_pressed():   
        audio.play(audio.SoundEffect())
        for i in range(buffer):
            radio.send('B')
            sleep(1)

    if radio.receive() == "A":
        display.show("A")
        move(74.25,-75,3000)


    if radio.receive() == "B":
        display.show("B")
        move(-74.25,75,3000)



    


    

