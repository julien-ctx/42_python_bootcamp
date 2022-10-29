#https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
#https://towardsdatascience.com/the-simplest-cleanest-method-for-tracking-a-for-loops-progress-and-expected-run-time-in-python-972675392b3

import time
from time import sleep

def ft_progress(lst):
	START = time.time()
	for x in lst:
		elapsed = 0
		while not elapsed:
			elapsed = time.time() - START
		eta = len(lst) * elapsed / (x + 1) - elapsed
		perc = int(elapsed * 100 / (elapsed + eta))
		# print("Current: {:.2f}".format(now), end = "\r")
		# print("Estimated: {:.2f}".format(estimated), end = "\r")
		print("\r", end = '')
		print("ETA:\t {:.2f}".format(eta), end = '')
		print("s [" + str(perc) + "%]", end = '')
		print("[] ", end = '')
		print(str(x) + "/" + str(len(lst) - 1), end = '')
		print(" | elapsed time " + "{:.2f}".format(elapsed) + "s", end = '')
		yield x

if __name__ == "__main__":
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		sleep(0.01)
	print()
	print(ret)
