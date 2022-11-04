def ft_map(f, i):
	"""Map the function to all elements of the iterable.
	Args:
	f: a function taking an iterable.
	i: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	try:
		iter(i)
	except TypeError as e:
		print("TypeError: " + str(e))
		return None
	if callable(f):
		return [f(x) for x in i]
	else:
		print("TypeError: f is not a function")
		return None
 