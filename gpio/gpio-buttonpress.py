from gpiozero import Button

button = Button(21)

button.wait_for_press()
print("You pushed me")

  
