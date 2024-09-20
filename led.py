from gpiozero import LED     # import led from gpiozero
from time import sleep       # import sleep from time


led=LED(18)                  # define gpio.bcm pin 18 as led


led.blink(0.25,0.25)         # blink led (0.25s on 0.25s off)
sleep(100)                   # sleep to prevent the program from exiting
