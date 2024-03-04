# Imports go at the top
from cyberbot import *
from microbit import *
import radio
radio.on()

while True:
    
    if button_a.is_pressed():
        audio.play(audio.SoundEffect())
        radio.send('A')
        
    elif button_b.is_pressed():   
        audio.play(audio.SoundEffect())
        radio.send('B')

    if radio.receive() == "A":
        display.show("A")

    if radio.receive() == "B":
       display.show("B")

print("x")
