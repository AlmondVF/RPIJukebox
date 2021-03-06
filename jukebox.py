import gpiozero, time, random, sys, vlc, signal
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

#setting which mp3 folder to use
if len(sys.argv) <=1:
    print('Please specify a folder') #for testing, won't be kept for non-lcd V1
    sys.exit(1)
folder = sys.argv[1]
files = glob.glob(folder+"/*.mp3")
if len(files) == 0:
    print('No mp3 files in directory', folder,'..exiting') #for testing, won't be kept for non-lcd V1
    sys.exit(1)

#vlc player setup
player = vlc.MediaPlayer()
#playlist setup
medialist = vlc.MediaList(files)
#linking it all
mlplayer = vlc.MediaListPlayer()
mlplayer.set_media_player(player)
mlplayer.set_media_list(medialist)

#defining the shutdown button
def shutdown():
    check_call(['sudo', 'poweroff'])
while True:
    if playpausebutton.is_pressed:
        if mlplayer.is_playing():
            mlplayer.pause() #pauses the music when the playpausebutton is pressed
        else:
            mlplayer.play() #plays the music when the playpausebutton is pressed
    elif stopbutton.is_pressed:
        mlplayer.stop() #stops the music when the stopbutton is pressed
    elif trackforwardsbutton.is_pressed:
        mlplayer.previous() #skips forwards one track when the trackforwardsbutton is pressed
    elif trackbackbutton.is_pressed:
        mlplayer.next() #skips backwards one track when the trackbackbutton is pressed
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
