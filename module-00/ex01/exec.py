import sys
arg = " ".join(sys.argv[1::])
if (len(sys.argv) == 1):
	print ((arg.swapcase()) [::-1], end = '')
else:
	print ((arg.swapcase()) [::-1])
