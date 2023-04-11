import time
import board
import analogio

# Set up analog input pin
analog_in = analogio.AnalogIn(board.A0)

# Loop forever, reading and printing the analog input value
while True:
    # Read the analog input value and convert it to a voltage
    analog_voltage = analog_in.value / 65535 * 3.3
   
    # Convert the voltage to a distance in centimeters using the formula provided in the datasheet
    distance_cm = 41.382 * analog_voltage**(-1.146)
   
    # Print the distance in centimeters
    print("Distance: {:.2f} cm".format(distance_cm))
   
    # Delay for a short period of time before repeating the loop
    time.sleep(0.1)