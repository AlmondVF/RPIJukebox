from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(2)
while True:
    if button.is_pressed:
        if led.on:
            led.off
            sleep(0.5)
        elif led.off:
            led.on
            sleep(0.5)
    sleep(0.1)
