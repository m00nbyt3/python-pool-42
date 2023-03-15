import time

def main():
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret+=(elem+3) %5
		time.sleep(0.01) 
	print()
	print(ret)

def ft_progress(listy):
	otime = time.time()
	for i in listy:
		ctime = time.time() - otime
		left = (ctime/(i+1))*(len(listy)-(i+1))
		per = int((i+1)*100/len(listy))
		eqs = int(((per + 1) * 20) / 100)
		spc = int(20 - eqs)
		print(f"ETA: {left:0.2f}s ",end="")
		print(f"[{per:3d}%] [",end="")
		print(eqs * "=",end="")
		print(">" + (spc *" ") + "] ",end="")
		print(f"{i+1}/{len(listy)}",end="")
		print(f" | elapsed time {ctime:.2f}s",end="\r")
		yield i
if __name__ == '__main__':
	main()