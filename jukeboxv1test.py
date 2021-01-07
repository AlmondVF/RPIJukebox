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
while True:
    for song in Music:
        if song.endswith('.mp3'):
            file = '/home/almondvf/Music/' + song
            pygame.mixer.music.load(str(file))
            pygame.mixer.music.play()
            print('Playing ' + song)
            while pygame.mixer.music.get_busy == True:
                led1.on()
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
                sleep(0.25)
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
                led2.on()
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
                sleep(0.25)
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
                led1.off()
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
                led3.on()
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
                sleep(0.25)
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
                led2.off()
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
                led4.on()
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
                led3.off()
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
                sleep(0.25)
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
                led5.on()
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
                led4.off()
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
                sleep(0.25)
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
                led6.on()
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
                led5.off()
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
                sleep(0.25)
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
                led7.on()
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
                led6.off()
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
                sleep(0.25)
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
                led8.on()
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
                led7.off()
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
                sleep(0.25)
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
                led9.on()
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
                led8.off()
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
                sleep(0.25)
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
                led10.on()
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
                led9.off()
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
                sleep(0.25)
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
                led11.on()
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
                led10.off()
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
                sleep(0.25)
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
                led12.on()
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
                led11.off()
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
                sleep(0.25)
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
                led13.on()
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
                led12.off()
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
                sleep(0.25)
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
                led14.on()
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
                led13.off()
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
                sleep(0.25)
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
                led14.off()
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
                
