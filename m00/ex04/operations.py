import sys

nums = sys.argv
try:
	assert len(nums) != 1
	assert len(nums) == 3, "Too many args!"
	print("Sum:        " + str(int(nums[1]) + int(nums[2])))
	print("Difference: " + str(int(nums[1]) - int(nums[2])))
	print("Product:    " + str(int(nums[1]) * int(nums[2])))
	print("Quotient:   " + str(int(nums[1]) / int(nums[2])))
	print("Remainder:  " + str(int(nums[1]) % int(nums[2])))


except AssertionError as msg:
	print(msg)
except ValueError:
	print("Not a number!")
except ZeroDivisionError:
	print("Quotient:   ERROR (division by zero)")
	print("Remainder:  ERROR (modulo by zero)")
