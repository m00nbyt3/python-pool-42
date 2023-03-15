import sys

argv = sys.argv
if len(argv) == 1:
	exit()
try:
	assert len(argv) != 1
	assert len(argv) == 2, "More than one argument are provided"
	if int(argv[1]) == 0:
		print("I'm Zero") 
	elif int(argv[1]) % 2:
		print("I'm Odd")
	else:
		print("I'm Even")
except ValueError:
	print("Not a number!")
except AssertionError as msg:
	print(msg)
