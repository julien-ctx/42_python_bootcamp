import numpy as np
import random

class NumPyCreator:

	def from_list(self, lst):
		return np.array(lst)
	
	def from_tuple(self, lst):
		return np.array(lst)
	
	def from_iterable(self, itr):
		return np.fromiter(itr, int)
	
	def from_shape(self, shape, value = 0):
		return np.full(shape, value)
		
	def random(self, shape):
		return np.full(shape, random.randint(-2147483648, 2147483647))
	
	def identity(self, n):
		return np.identity(n)

if __name__ == "__main__":

	test = NumPyCreator()
	print(test.from_list([1, 3, 4]))
	print()
	print(test.from_tuple((1, 3, 4)))
	print()
	print(test.from_iterable([1, 3, 4]))
	print()
	print(test.from_shape((8, 1)))
	print()
	print(test.random((8, 1)))
	print()
	print(test.identity(7))
