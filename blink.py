import time
from machine import Pin

# Set up the internal LED pin as an output
led = Pin("LED", Pin.OUT)

n = 0

# Loop forever to blink the light
while True:
    led.toggle()  # Switch the LED on if off, or off if on
    print(f"{n}. Hello Bink!")
    time.sleep(0.5)  # Wait half a second
    
    n += 1
    if (n > 10): break

# finally make the led off
led.off()

