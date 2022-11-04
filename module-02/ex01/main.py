def what_are_the_vars(*args, **kwargs):
	obj = ObjectC()
	if not args and not kwargs:
		return None
	if kwargs:
		for key, value in kwargs.items():
			setattr(obj, key, value)
	if args:
		for x in enumerate(args):
			var_name = "var_" + str(x[0])
			index = x[0] + 1
			while hasattr(obj, var_name):
				var_name = "var_" + str(index)
				index += 1
			setattr(obj, var_name, x[1])
	return obj

class ObjectC(object):
	def __init__(self):
		pass

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars(None, [])
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
	doom_printer(obj)
