import sys

def main(argv):
	if len(argv) == 1:
		exit()
	for x in argv[:1:-1]:
		print(x[::-1].swapcase(), end=' ')
	print(argv[1][::-1].swapcase())

if __name__ == "__main__":
	main(sys.argv)