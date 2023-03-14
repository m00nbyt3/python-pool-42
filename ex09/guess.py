import random

number = random.randint(1, 99)
attempts = 0
while True:
	attempts += 1
	print("Guess the number!!! (1 - 99)")
	guess = input(">> ")
	if guess == "My brownies taste like pipsa":
		print("~~" + str(number) + "~~\n")
		attempts -= 1
		continue
	if guess == "exit":
		print("Bye you loser")
		exit()
	if not guess.isnumeric():
		print("\nThis is not a number :(\n")
		continue
	elif int(guess) < 1 or int(guess) > 99:
		print("\nNumber not in range :O\n")
		continue
	elif int(guess) == number:
		num = 0
		break
	else:
		if int(guess) < number:
			print("\nWrong number! Try with a number a little bigger ;)")
		if int(guess) > number:
			print("\nWrong number! Try with a number a little smaller ;)")
	print("")
if number == 42:
	print("\nThe answer to the ultimate question of life, the universe and everything is 42.")
if attempts == 1:
	print("\nWOW YOU GUESSED IT AT FIRST TRY, CONGRATS :000")
else:
	print("\nYou guessed the number in only " + str(attempts) + " attempts!!")