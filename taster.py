# Bibliotheken laden
from gpiozero import Button 
from gpiozero import LED
import time



i=0

def ledonoff():
    global i
    if i==0:
        led.on()
        i=1
    else:
        led.off()
        i=0

# Initialisierung von GPIO27 als Button (Eingang)
button = Button(27)
led= LED(18)



while True:

    button.wait_for_press() 
    ledonoff()
    time.sleep(0.5)
