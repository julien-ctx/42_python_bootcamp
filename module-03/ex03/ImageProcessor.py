import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

class ImageProcessor:

	def load(self, path = None):
		if not path:
			raise Exception("No path provided")
		try:
			img = Image.open(path)
			width, height = img.size
			print("Loading image of dimensions " + str(width) + " x " + str(height))
			img.show()
			return np.asarray(img)
		except FileNotFoundError as e:
			print("Exception: FileNotFoundError -- strerror: No such file or directory")
			return None
		except OSError as e:
			print("Exception: OSError -- strerror: None")
			return None
		
	def display(self, array):
		img = Image.fromarray(array)
		img.show()

if __name__ == "__main__":
	img = ImageProcessor()
	arr = img.load("empty.jpeg")
	print()
	img.load("fake.png")
	print()
	arr = img.load("42ai.jpeg")
	print()
	print(arr)
	img.display(arr)
