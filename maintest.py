import gpiozero, time, random, sys, vlc, signal
from subprocess import check_call
#button for skipping back one track
trackbackbutton = gpiozero.Button(2)
#button for play/pause control
playpausebutton = gpiozero.Button(3)
#button for skipping forwards one track
trackforwardsbutton = gpiozero.Button(4)
#button to stop the music and set track = 0
stopbutton = gpiozero.Button(5)
#button to shutdown the pi
shutdownbutton = gpiozero.Button(6)
#button to change the led mode
ledbutton = gpiozero.Button(7)

#LED setup
led1 = gpiozero.PWMLED(9)
led2 = gpiozero.PWMLED(10)
led3 = gpiozero.PWMLED(11)
led4 = gpiozero.PWMLED(12)
led5 = gpiozero.PWMLED(13)
led6 = gpiozero.PWMLED(14)
led7 = gpiozero.PWMLED(15)
led8 = gpiozero.PWMLED(16)
led9 = gpiozero.PWMLED(17)
led10 = gpiozero.PWMLED(18)
led11 = gpiozero.PWMLED(19)
led12 = gpiozero.PWMLED(20)
led13 = gpiozero.PWMLED(21)
led14 = gpiozero.PWMLED(22)
led15 = gpiozero.PWMLED(23)
led16 = gpiozero.PWMLED(24)
led17 = gpiozero.PWMLED(25)
led18 = gpiozero.PWMLED(26)
leds = gpiozero.PWMLED(9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)

#defining the shutdown button
def shutdown():
    check_call(['sudo', 'poweroff'])
while True:
    if playpausebutton.is_pressed:
        print('button pressed')
    elif stopbutton.is_pressed:
        print('button pressed')
    elif trackforwardsbutton.is_pressed:
        print('button pressed')
    elif trackbackbutton.is_pressed:
        print('button pressed')
    elif shutdownbutton.when_pressed:
        shutdown() #shuts down the pi when the shutdownbutton is pressed
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
