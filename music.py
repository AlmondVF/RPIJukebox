import os
import pygame
import time

pygame.init()
pygame.mixer.init()

ListsOfSongs = os.listdir('/home/almondvf/Music')

for song in ListsOfSongs:
    if song.endswith('.mp3'):
        file_path = '/home/almondvf/Music/' + song
        pygame.mixer.music.load(str(file_path))
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.stop()
        time.sleep(5)
        pygame.mixer.music.play()
        print('Playing ' + song)
        while pygame.mixer.music.get_busy() == True:
            continue
