import os
import pygame
from time import sleep
import gpiozero, random, sys, signal
#button to stop the music and set track = 0
stopbutton = gpiozero.Button(2)
#button for play/pause control
playpausebutton = gpiozero.Button(3)
#shutdown button

#defining the controls
def controls():
    if stopbutton.is_pressed:
        if flag2 == 0:
            print('stopping')
            pygame.mixer.music.stop()
            sleep(0.5)
            flag2 = 1
        elif flag2 == 1:
            print('starting')
            pygame.mixer.music.play()
            sleep(0.5)
            flag2 = 0
    elif playpausebutton.is_pressed:
        if flag1 == 0:
            print('paused')
            pygame.mixer.music.pause()
            sleep(0.5)
            flag1 = 1
        elif flag1 == 1:
            print('playing')
            pygame.mixer.music.unpause()
            sleep(0.5)
            flag1 = 0
#LEDs
led1 = gpiozero.LED(5)
led2 = gpiozero.LED(6)
led3 = gpiozero.LED(7)
led4 = gpiozero.LED(8)
led5 = gpiozero.LED(9)
led6 = gpiozero.LED(10)
led7 = gpiozero.LED(11)
led8 = gpiozero.LED(12)
led9 = gpiozero.LED(13)
led10 = gpiozero.LED(14)
led11 = gpiozero.LED(15)
led12 = gpiozero.LED(16)
led13 = gpiozero.LED(17)
led14 = gpiozero.LED(18)
#flag to make playpause button work
flag1 = 0
#flag to make stopstart button work
flag2 = 0
pygame.init()
pygame.mixer.init()

Music = os.listdir('/home/almondvf/Music')

for song in Music:
    if song.endswith('.mp3'):
        file = '/home/almondvf/Music/' + song
        pygame.mixer.music.load(str(file))
        pygame.mixer.music.play()
        print('Playing ' + song)led1.on()
        controls()
        sleep(0.25)
        controls()
        led2.on()
        controls()
        sleep(0.25)
        controls()
        led1.off()
        controls()
        led3.on()
        controls()
        sleep(0.25)
        controls()
        led2.off()
        controls()
        led4.on()
        controls()
        led3.off()
        controls()
        sleep(0.25)
        controls()
        led5.on()
        controls()
        led4.off()
        controls()
        sleep(0.25)
        controls()
        led6.on()
        controls()
        led5.off()
        controls()
        sleep(0.25)
        controls()
        led7.on()
        controls()
        led6.off()
        controls()
        sleep(0.25)
        controls()
        led8.on()
        controls()
        led7.off()
        controls()
        sleep(0.25)
        controls()
        led9.on()
        controls()
        led8.off()
        controls()
        sleep(0.25)
        controls()
        led10.on()
        controls()
        led9.off()
        controls()
        sleep(0.25)
        controls()
        led11.on()
        controls()
        led10.off()
        controls()
        sleep(0.25)
        controls()
        led12.on()
        controls()
        led11.off()
        controls()
        sleep(0.25)
        controls()
        led13.on()
        controls()
        led12.off()
        controls()
        sleep(0.25)
        controls()
        led14.on()
        controls()
        led13.off()
        controls()
        sleep(0.25)
        controls()
        led14.off()
        controls()
        while pygame.mixer.music.get_busy() == True:
            continue
