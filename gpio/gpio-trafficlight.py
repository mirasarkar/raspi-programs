from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

# 5V
# 5V
# GP14
# GP15 => Buzzer
# GP18
# GND
# GP23
# GP24
# GND
# GP25 => Red
# GP8  => Amber
# GP7  => Green
# DNC
# GND
# GP12
# GND
# GP16
# GP20
# GP21 => Button

buzzer = Buzzer(15)
lights = TrafficLights(25, 8, 7)
button = Button(21)

while True:
    button.wait_for_press()
    lights.green.on()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.red.on()
    sleep(1)
    lights.off()
