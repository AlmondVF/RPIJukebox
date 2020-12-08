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

ListsOfSongs = os.listdir('/home/almondvf/Music')

for song in ListsOfSongs:
    if song.endswith('.mp3'):
        file_path = '/home/almondvf/Music/' + song
        pygame.mixer.music.load(str(file_path))
        pygame.mixer.music.play()
        if stopbutton.is_pressed:
            pygame.mixer.music.stop()
        elif playpausebutton.is_pressed:
            if pygame.mixer.music.get_busy() == True:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.play()
        elif trackforwardsbutton.is_pressed:
            do something
        elif trackbackbutton.is_pressed:
            do something else
        print('Playing ' + song)
        while pygame.mixer.music.get_busy() == True:
            continue
elif ledbutton.is_pressed:
    if ledmode = ledmode1:
        ledmode = ledmode2
    elif ledmode = ledmode2:
        ledmode = ledmode3
    elif ledmode = ledmode3:
        ledmode = ledmode4
    elif ledmode = ledmode4:
        ledmode = ledmode1

#First LED mode is flash on off on off ...
ledmode1 = {
while True:
time.sleep(1)
leds.value = 0 #LEDs are off
time.sleep(1)
leds.value = 1 #LEDs are on
}

#second Led mode is fade on fade off ...
ledmode2 = {
while True:
leds.pulse() #LEDs fade in and out continiously
}

#third LED mode is always on
ledmode3 = {
while True:
leds.value = 1 #LEDs are on
}

#fourth LED mode is always off
ledmode4 = {
while True:
leds.value = 0 #LEDs are off
}

signal.pause()
