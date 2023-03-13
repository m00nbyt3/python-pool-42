import string
import sys

def text_analyzer(text):
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

if len(sys.argv) == 2:
	text = sys.argv[1]
else:
	text = input("Input text: ")
text_analyzer(text)