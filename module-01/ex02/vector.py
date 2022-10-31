class Vector:
	def __init__(self, values):
		if not all(isinstance(elem, list) for elem in values):
			print("Error: please enter values in a correct format.")
			exit(1)
		if len(values) == 1:
			if len(values[0]) < 2:
				print("Error: several float values are needed in the list")
				exit(1)
			self.shape = (1, len(values[0]))
		else:
			for elem in values:
				if len(elem) != 1:
					print("Error: only one float value is allowed in the list")
					exit(1)
			self.shape = (len(values), 1)
		self.values = values

	def getShape(self):
		return self.shape
