import numpy as np

class ScrapBooker:
	def crop(self, array, dim, position = (0, 0)):
		"""
		Crops the image as a rectangle via dim arguments (being the new height
		and width of the image) from the coordinates given by position arguments.
		Args:
		-----
		array: numpy.ndarray
		dim: tuple of 2 integers.
		position: tuple of 2 integers.
		Return:
		-------
		new_arr: the cropped numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		if dim[0] >= dim[1] or position[1] >= position[1]:
			return None
		return array[position[0]:(dim[0] + position[0]), position[1]:(dim[1] + position[1])]

	def thin(self, array, n, axis):
		"""
		Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
		Args:
		-----
		array: numpy.ndarray.
		n: non null positive integer lower than the number of row/column of the array
		(depending of axis value).
		axis: positive non null integer.
		Return:
		-------
		new_arr: thined numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		if axis not in (0, 1) or n < 1:
			return None
		if axis:
			max_len = array.shape[0]
			if n > array.shape[0]:
				return None
		else:
			max_len = array.shape[1]
			if n > array.shape[1]:
				return None
		axis = 1 if axis == 0 else 0
		i = n - 1
		while (i < max_len):
			array = np.delete(array, i, axis)
			i += (n - 1)
			max_len -= 1
		return array


	def juxtapose(self, array, n, axis):
		"""
		Juxtaposes n copies of the image along the specified axis.
		Args:
		-----
		array: numpy.ndarray.
		n: positive non null integer.
		axis: integer of value 0 or 1.
		Return:
		-------
		new_arr: juxtaposed numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""

	def mosaic(self, array, dim):
		"""
		Makes a grid with multiple copies of the array. The dim argument specifies
		the number of repetition along each dimensions.
		Args:
		-----
		array: numpy.ndarray.
		dim: tuple of 2 integers.
		Return:
		-------
		new_arr: mosaic numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""

if __name__ == "__main__":
	spb = ScrapBooker()
	arr1 = np.arange(0, 25).reshape(5, 5)
	
	print(spb.crop(arr1, (3, 1), (1,0)))
	print()

	arr2 = np.array("A B C D E F G H I J K".split() * 6).reshape(-1, 11)
	print(spb.thin(arr2, 3, 0))
	# print()

	# arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
	# print(spb.juxtapose(arr3, 3, 1))
