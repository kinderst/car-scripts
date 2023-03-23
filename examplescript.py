import time
import os

# channel 1 (steering), 1500
# echo -n -e "\x84\x01\x70\x2e" > /dev/ttyACM0

# https://stackoverflow.com/questions/29286687/how-do-you-echo-quotes-using-pythons-os-system
# or try "w" instead of "a", etc: https://docs.python.org/3/tutorial/inputoutput.html ctrl+f open
# maybe add new line (\n) to end? not sure how bytes read by file
# replace hello.txt with /dev/ttyACM0
print("starting in 2 sec")
time.sleep(2)
print("initializing, setting to 1500 x70 x2e")
# write 
cmd = r'sudo echo -n -e "\x84\x01\x70\x2e" > /dev/ttyACM0'
# cmd = r'echo -n -e "\x84\x01\x70\x2e" > hello.txt'
os.system(cmd)
# sleep one second
print("sleeping...")
time.sleep(1)
while True:
	# create serial bytes array
	serial_bytes = []

	# command byte, maestro
	serial_bytes.append("x84")

	print("enter channel, (or anything else to break): ")
	channel = input()
	channel = int(channel)
	if channel < 1 or channel > 2:
		break
	channel_hex = hex(channel)[1:]
	serial_bytes.append(channel_hex)

	print("enter target (times 4 for quarter ms): ")
	target = input()
	target = int(target)

	# second and third bytes need to be defined specifically like this:
	# https://www.pololu.com/docs/0J40/5.e
	second_byte = target & 0x7F
	third_byte = (target >> 7) & 0x7F;

	second_hex = hex(second_byte)[1:]
	third_hex = hex(third_byte)[1:]
	serial_bytes.append(second_hex)
	serial_bytes.append(third_hex)


	print(serial_bytes)

	#echo_string = r'sudo echo -n -e "' + serial_bytes[0] +  serial_bytes[1] +  + serial_bytes[2] +  + serial_bytes[3] + '" > /dev/ttyACM0'
	echo_string = r'sudo echo -n -e "\\' + serial_bytes[0] + r'\\' + serial_bytes[1] + r'\\' + serial_bytes[2] + r'\\' + serial_bytes[3] + r'" > /dev/ttyACM0'
	# \x84\x01\x70\x2e" > /dev/ttyACM0'
	print(echo_string)
	os.system(echo_string)
	
print("calibrated forward steering angle (4x!!! qms)?: ")
calibrated_steer_val = input()
calibrated_steer_val = int(calibrated_steer_val)
print("calibrated_steer_val: ", calibrated_steer_val)
print("calibrated acceleration value (4x!!!)?: ")
calibrated_accel_val = input()
calibrated_accel_val = int(calibrated_accel_val)
print("calibrated_accel_val: ", calibrated_accel_val)
print("if these values are correct, type y")
cont_string = input()
cont_string = str(cont_string)
if cont_string == 'y':
	print("you are autonomous, beginning forward for one second operation:")
	print("sleeping for 1 second: ")
	time.sleep(1)
	print("setting steering straight: ")
	serial_bytes = []
	# command byte, maestro
	serial_bytes.append("x84")
	# we are setting steering, so channel 1:
	serial_bytes.append("x1")
	# write the value bytes, i.e. second and third data bytes:
	# target, i.e. calibrated steer val in quarter ms
	second_byte = calibrated_steer_val & 0x7F
	third_byte = (calibrated_steer_val >> 7) & 0x7F;

	second_hex = hex(second_byte)[1:]
	third_hex = hex(third_byte)[1:]
	serial_bytes.append(second_hex)
	serial_bytes.append(third_hex)
	print("steering command:")
	print(serial_bytes)
	echo_string = r'sudo echo -n -e "\\' + serial_bytes[0] + r'\\' + serial_bytes[1] + r'\\' + serial_bytes[2] + r'\\' + serial_bytes[3] + r'" > /dev/ttyACM0'
	print(echo_string)
	os.system(echo_string)

	print("assuming wheels not spinning, and calibration accel val properly set, steering forward, otherwise yikes")

	print("sleeping for one second, then beginning: +200 qms (50) forward for 1s, then back to still")
	time.sleep(1)

	# go:
	updated_accel = calibrated_accel_val + 200
	# create serial bytes
	serial_bytes = []
	# command byte, maestro
	serial_bytes.append("x84")
	# we are setting steering, so channel 1:
	serial_bytes.append("x2")
	# write the value bytes, i.e. second and third data bytes:
	# target, i.e. calibrated steer val in quarter ms
	second_byte = updated_accel & 0x7F
	third_byte = (updated_accel >> 7) & 0x7F;

	second_hex = hex(second_byte)[1:]
	third_hex = hex(third_byte)[1:]
	serial_bytes.append(second_hex)
	serial_bytes.append(third_hex)
	print("printing serial bytes, then the echo string for it, for channel 2!")
	print(serial_bytes)
	echo_string = r'sudo echo -n -e "\\' + serial_bytes[0] + r'\\' + serial_bytes[1] + r'\\' + serial_bytes[2] + r'\\' + serial_bytes[3] + r'" > /dev/ttyACM0'
	print(echo_string)
	os.system(echo_string)
	print("sleeping 1 second:")
	time.sleep(1)
	print("stopping:")
	# create serial bytes
	serial_bytes = []
	# command byte, maestro
	serial_bytes.append("x84")
	# we are setting steering, so channel 1:
	serial_bytes.append("x2")
	# write the value bytes, i.e. second and third data bytes:
	# target, i.e. calibrated steer val in quarter ms
	second_byte = calibrated_accel_val & 0x7F
	third_byte = (calibrated_accel_val >> 7) & 0x7F;

	second_hex = hex(second_byte)[1:]
	third_hex = hex(third_byte)[1:]
	serial_bytes.append(second_hex)
	serial_bytes.append(third_hex)
	print("printing serial bytes, then the echo string for it, for channel 2!")
	print(serial_bytes)
	echo_string = r'sudo echo -n -e "\\' + serial_bytes[0] + r'\\' + serial_bytes[1] + r'\\' + serial_bytes[2] + r'\\' + serial_bytes[3] + r'" > /dev/ttyACM0'
	print(echo_string)
	os.system(echo_string)
	print("ending program")