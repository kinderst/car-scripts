import time
import board
import digitalio

import inspect

# print("wtf")
# print(inspect.getmembers(board))
# print("ok")
# print(dir(board))

# Set up digital input pin
digital_in = digitalio.DigitalInOut(board.D18)
digital_in.direction = digitalio.Direction.INPUT

# Loop forever, reading and printing the digital input value
while True:
    # Read the digital input value
    digital_value = digital_in.value
   
    # If the digital input value is high, the sensor is detecting an object
    # If the digital input value is low, the sensor is not detecting an object
    if digital_value:
        print("Object detected")
    else:
        print("No object detected")
   
    # Delay for a short period of time before repeating the loop
    time.sleep(0.1)