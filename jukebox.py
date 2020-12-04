import gpiozero, time, random, sys, vlc
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
    check_call(['sudo', 'shutdown', '-h', 'now'])
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

#First LED mode
ledmode1 ={
while True:

     }
#second Led mode
ledmode2 = {
while True:

}
