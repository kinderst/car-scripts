import odroid_wiringpi as wpi
import time
 
serial = wpi.serialOpen('/dev/ttyS0', 115200)
 
while True:
        input_str = 'Serial Input> '
        wpi.serialPuts(serial, input_str)
        time.sleep(0.1)
 
        output_str = 'Serial Output> '
        while wpi.serialDataAvail(serial):
                output_str += chr(wpi.serialGetchar(serial))
        print(output_str)
 
wpi.serialClose(serial)