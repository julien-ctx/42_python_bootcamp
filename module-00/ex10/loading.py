#https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
#https://towardsdatascience.com/the-simplest-cleanest-method-for-tracking-a-for-loops-progress-and-expected-run-time-in-python-972675392b3

import time
from time import sleep
import sys

def ft_progress(lst):
	START = time.time()
	for x in lst:
		elapsed = 0
		size = len(lst)
		while not elapsed:
			elapsed = time.time() - START
		eta = size * elapsed / (x + 1) - elapsed
		perc = int(elapsed * 100 / (elapsed + eta))
		sys.stdout.write("\033[K")
		print('\r', end = '')
		print("ETA:\t {:.2f}".format(eta), end = '')
		print("s [" + str(perc) + "%]", end = '')
		print("[", end = '')
		for i in range(int(perc / 5)):
			print("=", end = '')
		print(">", end = '')
		for i in range(20 - int(perc / 5)):
			print(" ", end = '')
		print("] ", end = '')
		print(str(x + 1) + "/" + str(size), end = '')
		print(" | elapsed time " + "{:.2f}".format(elapsed) + "s", end = '')
		if lst.index(x) == size - 1:
			print("\n...", end = '')
		yield x

if __name__ == "__main__":
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		sleep(0.01)
	print()
	print(ret)
	print("Next test:")
	listy2 = range(3333)
	ret2 = 0
	for elem in ft_progress(listy2):
		ret2 += elem
		sleep(0.005)
	print()
	print(ret2)
