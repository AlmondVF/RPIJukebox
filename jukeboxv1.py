import os
import pygame
from time import sleep
import gpiozero, random, sys, signal
#button to stop the music and set track = 0
stopbutton = gpiozero.Button(2)
#button for play/pause control
playpausebutton = gpiozero.Button(3)
#shutdown button

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
        print('Playing ' + song)
        while True:
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
            elif True:
                if playpausebutton.is_pressed:
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
                while pygame.mixer.music.get_busy() == True:
                    continue
                    led1.on()
                    sleep(0.25)
                    led2.on()
                    sleep(0.25)
                    led1.off()
                    led3.on()
                    sleep(0.25)
                    led2.off()
                    led4.on()
                    led3.off()
                    sleep(0.25)
                    led5.on()
                    led4.off()
                    sleep(0.25)
                    led6.on()
                    led5.off()
                    sleep(0.25)
                    led7.on()
                    led6.off()
                    sleep(0.25)
                    led8.on()
                    led7.off()
                    sleep(0.25)
                    led9.on()
                    led8.off()
                    sleep(0.25)
                    led10.on()
                    led9.off()
                    sleep(0.25)
                    led11.on()
                    led10.off()
                    sleep(0.25)
                    led12.on()
                    led11.off()
                    sleep(0.25)
                    led13.on()
                    led12.off()
                    sleep(0.25)
                    led14.on()
                    led13.off()
                    sleep(0.25)
                    led14.off()
pause()
