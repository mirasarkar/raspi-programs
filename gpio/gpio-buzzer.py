from gpiozero import LED, Button, Buzzer
from time import sleep

led = LED(17)
button = Button(2)
buzzer = Buzzer(18)

# When you push the button
# It buzzes for one second
# Then the led comes on for one second
# Then buzzes for one second
# Wait for one second

led.blink()
button.wait_for_press()
print("Mira and Daddy wrote this program.")
buzzer.on()
sleep(1)
buzzer.off()
led.on()
sleep(1)
led.off()
buzzer.on()
sleep(1)
buzzer.off()
sleep(1)
buzzer.beep()
sleep(10)
buzzer.off()
