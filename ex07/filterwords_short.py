import sys, string

if not (len(sys.argv) != 3 or sys.argv[1].isnumeric() or not sys.argv[2].isnumeric()):
	print([x for x in [''.join(c for c in w if c not in string.punctuation)
		for w in sys.argv[1].split()] if len(x) > int(sys.argv[2])])