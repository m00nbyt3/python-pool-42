import string
import sys

def text_analyzer(text=None):
	'''
This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.
	'''
	if not text:
		text = input("Input text: ")
	if not isinstance(text, str):
		print("Not a string")
		return
	upper = 0
	lower = 0
	pmark = 0
	space = 0
	for x in text:
		if x.isupper():
			upper += 1
		elif x.islower():
			lower += 1
		elif x in string.punctuation:
			pmark += 1
		elif x.isspace():
			space += 1
	print("- " + str(upper) + " upper letter(s)")
	print("- " + str(lower) + " lower letter(s)")
	print("- " + str(pmark) + " punctuation mark(s)")
	print("- " + str(space) + " space(s)")

def main(argv):
	text = None
	if len(sys.argv) == 2:
		text = sys.argv[1]
	elif len(sys.argv) != 1:
		print("More than one argument passed!")
		return()
	text_analyzer(text)

if __name__ == "__main__":
	main(sys.argv)