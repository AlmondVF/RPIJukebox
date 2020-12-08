from time import sleep
from pathlib import Path
import pygame
DIRECTORY = Path('/home/almondvf/Music')
pygame.mixer.init()

for fp in DIRECTORY.glob('*.mp3'):
    pygame.mixer.music.load(str(fp))
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        sleep(1)
