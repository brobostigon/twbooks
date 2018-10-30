import random
import speech
import os
import radio

from collections import namedtuple
from microbit import *

radio.on()
Die = namedtuple('Die', ['sides', 'bitmap'])

dice = (
    Die(2, '09990:00090:09990:09000:09990'),
    Die(4, '09090:09090:09990:00090:00090'),
    Die(6, '09990:09000:09990:09090:09990'),
    Die(8, '09990:09090:09990:09090:09990'),
    Die(10, '90999:90909:90909:90909:90999'),
    Die(12, '90999:90009:90999:90900:90999'),
    Die(20, '99999:00909:99999:90000:99900'),
)
def roll():
    steps = [
        Image('00000:00990:00090:00000:00000'),
        Image('00000:00090:00090:00090:00000'),
        Image('00000:00000:00090:00990:00000'),
        Image('00000:00000:00000:09990:00000'),
        Image('00000:00000:09000:09900:00000'),
        Image('00000:09000:09000:09000:00000'),
        Image('00000:09900:09000:00000:00000'),
        Image('00000:09990:00000:00000:00000'),
    ]
    display.show(steps, delay=100)
    display.show(steps, delay=100)

index = 0
redraw = True
while True:
    if redraw:
        die = dice[index]
        display.show(Image(die.bitmap))
        sleep(200)
        redraw = False

    if button_a.is_pressed():
        index -= 1
        index %= len(dice)
        redraw = True
    
    if button_b.is_pressed():
        roll()
        result = random.choice(range(1, die.sides + 1))
        display.scroll(str(result))
        speech.say(str(result))
        radio.send(str(result))
        #with open('result.txt', 'w') as results:
        #results.write(str(result))
        redraw = True
    if pin0.is_touched():
        incoming = radio.receive()
        display.scroll(str(incoming))