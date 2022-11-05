import os

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		if not filename:
			raise Exception("No file provided")
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		if os.path.exists(self.filename):
			self.f = open(self.filename, "r")
		else:
			raise Exception("File not found")

	def __enter__(self):
		all_lines = [line.replace('\n', '').replace(' ', '').replace('"', '').split(self.sep) for line in self.f]
		for line in all_lines:
			line = list(filter(None, line))
			if len(line) != len(all_lines[0]):
				print("File is corrupted")
				return None
		self.header = all_lines[0] if self.header else None
		if self.skip_top >= len(all_lines) or self.skip_bottom >= len(all_lines):
			print("Error: cannot slice data correctly.")
			return None
		self.data = all_lines[self.skip_top:len(all_lines) - self.skip_bottom]
		return self
		
	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.f.close()

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
		nested list (list(list, list, ...)) representing the data.
		"""
		return self.data

	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
		return self.header

if __name__ == "__main__":
	with CsvReader("good.csv", skip_top=1, skip_bottom=5, header=1) as f:
		if not f:
			exit(1)
		print(f.getheader())
		print()
		print(f.getdata())
	
	print()
	with CsvReader("bad.csv", header=1) as f:
		if not f:
			exit(1)
		print(f.getheader())
