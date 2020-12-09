import os
import pygame
import time
import gpiozero, random, sys, signal
from subprocess import check_call
#button for skipping back one track
trackbackbutton = gpiozero.Button(3)
#button for play/pause control
playpausebutton = gpiozero.Button(4)
#button for skipping forwards one track
trackforwardsbutton = gpiozero.Button(5)
#button to stop the music and set track = 0
stopbutton = gpiozero.Button(6)
#button to shutdown the pi
shutdownbutton = gpiozero.Button(7)
#button to change the led mode
ledbutton = gpiozero.Button(8)

#LED setup
leds = gpiozero.LEBboard(9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, pwm=True)

pygame.init()
pygame.mixer.init()

Music = os.listdir('/home/almondvf/Music')

for song in Music:
    if song.endswith('.mp3'):
        file = '/home/almondvf/Music/' + song
        pygame.mixer.music.load(str(file))
        pygame.mixer.music.play()
        print('Playing ' + song)
        while True:
            if stopbutton.gpiozero.is_pressed:
                pygame.mixer.music.stop()
            elif playpausebutton.gpiozero.is_pressed:
                if pygame.mixer.music.get_busy() == True:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.play()
        break
while pygame.mixer.music.get_busy() == True:
    continue
while True:
    if ledbutton.gpiozero.is_pressed:
        if ledmode = ledmode1():
        ledmode = ledmode2()
    elif ledmode = ledmode2():
        ledmode = ledmode3()
    elif ledmode = ledmode3():
        ledmode = ledmode4()
    elif ledmode = ledmode4():
        ledmode = ledmode1()

#First LED mode is flash on off on off ...
def ledmode1():
    while True:
        time.sleep(1)
        leds.gpiozero.value = 0 #LEDs are off
        time.sleep(1)
        leds.gpiozero.value = 1 #LEDs are on

#second Led mode is fade on fade off ...
def ledmode2():
    while True:
        leds.gpiozero.pulse() #LEDs fade in and out continiously


#third LED mode is always on
def ledmode3():
    while True:
        leds.gpiozero.value = 1 #LEDs are on


#fourth LED mode is always off
def ledmode4():
    while True:
        leds.gpiozero.value = 0 #LEDs are off


signal.pause()
