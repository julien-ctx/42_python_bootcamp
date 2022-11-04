import sys

def ft_reduce(f, i):
	"""Apply function of two arguments cumulatively.
	Args:
	f: a function taking an iterable.
	i: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.
	"""

	if callable(f):
		try:
			first = i[0]
			for second in range(1, len(i)):
				first = f(first, i[second])
			return first
		except TypeError as e:  
			sys.exit("TypeError: " + str(e))
	else:
		raise Exception("TypeError: f is not a function")
