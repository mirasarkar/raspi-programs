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

#buzzer = Buzzer(15)
lights = TrafficLights(25, 8, 7)
button = Button(21)
lights.green.on()
button.wait_for_press()
while True:
    sleep(5)
    lights.green.off()
    sleep(1)
    lights.amber.on()
    sleep(2)
    lights.amber.off()
    lights.red.on()
    #button.wait_for_press()
    sleep(5)
    if button.is_pressed:
        break
    lights.amber.on()
    sleep(1)
    lights.amber.off()
    lights.red.off()
    lights.green.on()
    
lights.green.off()
lights.amber.off()
lights.red.off()
