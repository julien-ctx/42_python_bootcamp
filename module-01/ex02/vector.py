#https://www.reddit.com/r/learnpython/comments/3cvgpi/can_someone_explain_radd_to_me_in_simple_terms_i/

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

	# Operator overloadings

	def __add__(self, vec):
		if self.shape != vec.shape:
			print("Error: addition is impossible of both objects don't have the same shape")
			return None
		else:
			if self.shape[0] == 1:
				return Vector([[x + y for x, y in zip(self.values[0], vec.values[0])]])
			else:
				return Vector([[x[0] + y[0]] for x, y in zip(self.values, vec.values)])
	
	def __radd__(self, vec):
		return self + vec

	def __sub__(self, vec):
		if self.shape != vec.shape:
			print("Error: addition is impossible of both objects don't have the same shape")
			return None
		else:
			if self.shape[0] == 1:
				return Vector([[x - y for x, y in zip(self.values[0], vec.values[0])]])
			else:
				return Vector([[x[0] - y[0]] for x, y in zip(self.values, vec.values)])
	
	def __rsub__(self, vec):
		return self - vec

	def __mul__(self, nb):
		if isinstance(nb, Vector):
			if nb.shape != self.shape:
				print("Error: multiplication of vector can only be executed if they have the same shape")
				return None
			if self.shape[0] == 1:
				return Vector([[x * y for x, y in zip(self.values[0], nb.values[0])]])
			else:
				return Vector([[x[0] * y[0]] for x, y in zip(self.values, nb.values)])
		else:
			if self.shape[0] == 1:
				return Vector([[x * nb for x in self.values[0]]])
			else:
				return Vector([[x[0] * nb] for x in self.values])
	
	def __rmul__(self, nb):
		return self * nb

	def __truediv__(self, nb):
		if isinstance(nb, Vector):
			if nb.shape != self.shape:
				print("Error: division of vector can only be executed if they have the same shape")
				return None
			if self.shape[0] == 1:
				if 0 in nb.values[0]:
					raise ZeroDivisionError("division by zero.")
				return Vector([[x / y for x, y in zip(self.values[0], nb.values[0])]])
			else:
				for x in nb.values:
					if not x[0]:
						raise ZeroDivisionError("division by zero.")
				return Vector([[x[0] / y[0]] for x, y in zip(self.values, nb.values)])
		else:
			if not nb:
				raise ZeroDivisionError("division by zero.")
			if self.shape[0] == 1:
				return Vector([[x / nb for x in self.values[0]]])
			else:
				return Vector([[x[0] / nb] for x in self.values])


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

	def T(self):
		lst = []
		if self.shape[0] == 1:
			for item in self.values[0]:
				tmp = []
				tmp.append(item)
				lst.append(tmp)
		else:
			tmp = []
			for item in self.values:
				tmp.append(item[0])
			lst.append(tmp)
		return lst

	def getShape(self):
		return self.shape
