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

	def dot(self, vec):
		if not isinstance(vec, Vector):
			print("Error: cannot execute dot product with a non-Vector variable")
			return None
		if self.shape == vec.getShape():
			nb = 0.0
			if self.shape[0] == 1:
				for item1, item2 in zip(self.values[0], vec.values[0]):
					nb += item1 * item2
			else:
				for item1, item2 in zip(self.values, vec.values):
					nb += item1[0] * item2[0]
			return nb
		else:
			print("Error: dot product cannot be executed if shapes are not the same")
			return None

	def getShape(self):
		return self.shape
