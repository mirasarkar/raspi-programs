from gpiozero import LED
from time import sleep

led = LED(17)
led.off()
i = 0
while i < 10:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    print(i)
    i=i+1
    
print("done")
