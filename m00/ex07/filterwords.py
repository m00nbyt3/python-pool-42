import sys
import string

def main():
	if len(sys.argv) != 3 or sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
		return
	words = sys.argv[1].split()
	new = []
	for x in words:
		punct = 0
		for c in x:
			if c in string.punctuation:
				punct += 1
		if (len(x) - punct) > int(sys.argv[2]):
			new.append(x)
	print(new)

if __name__ == '__main__':
	main()