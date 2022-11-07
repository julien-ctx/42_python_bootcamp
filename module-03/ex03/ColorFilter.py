import numpy as np
from ImageProcessor import ImageProcessor

# https://note.nkmk.me/en/python-numpy-image-processing/

class ColorFilter:
	def invert(self, array):
		"""
		Inverts the color of the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		return np.copy(255 - array)

	def to_blue(self, array):
		"""
		Applies a blue filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		blue = array.copy()
		blue[:, :, (0, 1)] = 0
		return blue

	def to_green(self, array):
		"""
		Applies a green filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		green = array.copy()
		green[:, :, (0, 2)] = 0
		return green

	def to_red(self, array):
		"""
		Applies a red filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		red = array.copy()
		red[:, :, (1, 2)] = 0
		return red

	def to_celluloid(self, array):
		"""
		Applies a celluloid filter to the image received as a numpy array.
		Celluloid filter must display at least four thresholds of shades.
		Be careful! You are not asked to apply black contour on the object,
		you only have to work on the shades of your images.
		Remarks:
		celluloid filter is also known as cel-shading or toon-shading.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		pass
		#couldn't understand the assignment

	def to_grayscale(self, array, filter, **kwargs):
		"""
		Applies a grayscale filter to the image received as a numpy array.
		For filter = 'mean'/'m': performs the mean of RBG channels.
		For filter = 'weight'/'w': performs a weighted mean of RBG channels.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		filter: string with accepted values in ['m','mean','w','weight']
		weights: [kwargs] list of 3 floats where the sum equals to 1,
		corresponding to the weights of each RBG channels.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if filter == 'w' or filter == 'weight':
			gray = kwargs['weights'][0] * array[:,:,2] + kwargs['weights'][1] * array[:,:,1] + kwargs['weights'][2] * array[:,:,0]
		else:
			return None
		return gray
		# couldn't understand the assignment for mean

if __name__ == "__main__":
	img = ImageProcessor()
	cf = ColorFilter()

	arr = img.load("elonmusk.jpg")
	img.display(cf.invert(arr))
	img.display(cf.to_blue(arr))
	img.display(cf.to_red(arr))
	img.display(cf.to_green(arr))
	img.display(cf.to_grayscale(arr, 'weight', weights = [0.0, 0.1, 0.9]))
