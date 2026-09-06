import time
from machine import Pin

# Set up the internal LED pin as an output
led = Pin("LED", Pin.OUT)

# Loop forever to blink the light
while True:
    led.toggle()  # Switch the LED on if off, or off if on
    print("Hello Bink!")
    time.sleep(0.5)  # Wait half a second
