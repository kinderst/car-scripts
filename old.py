












# with open("hello.txt", "a") as file:
# 	print("initializing, setting to 1500 x70 x2e")
# 	# write 
# 	file.write(r'echo -n -e "\x84\x01\x70\x2e" > /dev/ttyACM0')
# 	# sleep one second
# 	print("sleeping...")
# 	time.sleep(1)
# 	while True:
# 		# create serial bytes array
# 		serial_bytes = []

# 		# command byte, maestro
# 		serial_bytes.append("x84")

# 		print("enter channel: ")
# 		channel = input()
# 		channel = int(channel)
# 		channel_hex = hex(channel)[1:]
# 		serial_bytes.append(channel_hex)

# 		print("enter target (times 4 for quarter ms): ")
# 		target = input()
# 		target = int(target)

# 		# second and third bytes need to be defined specifically like this:
# 		# https://www.pololu.com/docs/0J40/5.e
# 		second_byte = target & 0x7F
# 		third_byte = (target >> 7) & 0x7F;

# 		second_hex = hex(second_byte)[1:]
# 		third_hex = hex(third_byte)[1:]
# 		serial_bytes.append(second_hex)
# 		serial_bytes.append(third_hex)


# 		print(serial_bytes)

# 		echo_string = 'echo -n -e "' + serial_bytes[0] +  '\\' + serial_bytes[1] + '\\' + serial_bytes[2] + '\\' + serial_bytes[3] + '" > /dev/ttyACM0'
# 		print(echo_string)
# 		file.write('echo -n -e "' + serial_bytes[0] +  '\\' + serial_bytes[1] + '\\' + serial_bytes[2] + '\\' + serial_bytes[3] + '" > /dev/ttyACM0')
	
		



# channel = 1
# target = 6000


# # print(hex(1500))

# # my_bin = 1500 & 0x7F
# # print(bin(my_bin))
# # print(hex(int(bin(my_bin),2)))
# # target_bytes = target.to_bytes(2, 'little')
# # print('target_bytes:')
# # print(target_bytes)
# serialBytes = []
# serialBytes.append("x84")
# serialBytes.append("x01")

# second_byte = target & 0x7F
# third_byte = (target >> 7) & 0x7F;
# serialBytes.append(hex(second_byte)[1:])
# serialBytes.append(hex(third_byte)[1:])
# # ok = (target >> 7) & 0x7F
# # print(hmm)
# # print(hex(hmm)[1:])
# # print(ok)

# print(serialBytes)

# serialBytes[0] = 0x84; # Command byte: Set Target.
# serialBytes[1] = channel; # First data byte holds channel number.
# serialBytes[2] = target & 0x7F; # Second byte holds the lower 7 bits of target.
# serialBytes[3] = (target >> 7) & 0x7F;   # Third data byte holds the bits 7-13 of target.