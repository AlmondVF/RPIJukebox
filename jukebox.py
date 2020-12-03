import gpiozero, time, random, sys, vlc
from subprocess import check_call
#button for changing playlist
playlistbutton = gpiozero.Button(2)
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
if len(sys.argv) <1:
    print('Please specify a folder') #for testing, won't be kept for non-lcd V1
    sys.exit(1)
folder1 = sys.argv[1]
files = glob.glob(folder1="/*.mp3")
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
            mlplayer.pause()
        else:
            mlplayer.play()
    elif stopbutton.is_pressed:
        mlplayer.stop()
    elif trackforwardsbutton.is_pressed:
        mlplayer.previous()
    elif trackbackbutton.is_pressed:
        mlplayer.next()
    elif shutdownbutton.when_pressed:
        shutdown()
    elif playlistbutton.is_pressed:
