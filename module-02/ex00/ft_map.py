import sys

def ft_map(f, i):
	"""
		Map the function to all elements of the iterable.
		Args:
		f: a function taking an iterable.
		i: an iterable object (list, tuple, iterator).
		Returns:
		An iterable.
		None if the iterable can not be used by the function.
	"""
	if callable(f):
		try:
			for x in i:
				yield f(x)
		except TypeError as e:  
			sys.exit("TypeError: " + str(e))
	else:
		raise Exception("TypeError: f is not a function")
