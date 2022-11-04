def ft_filter(f, i):
	"""Filter the result of function apply to all elements of the iterable.
	Args:
	f: a function taking an iterable.
	i: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	
	if callable(f):
		try:
			for x in i:
				if f(x):
					yield x
		except TypeError as e:  
			sys.exit("TypeError: " + str(e))
	else:
		raise Exception("TypeError: f is not a function")
