from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()

#button.wait_for_press()
#print("You pushed me")
#led.on()  
#sleep(3)
#led.off()
  
