class GotCharacter:
	def __init__(self, first_name = None, is_alive = True):
		if first_name:
			self.first_name = first_name
		else:
			self.first_name = "Christophe"
		self.is_alive = True

class Stark(GotCharacter):
	'''A class representing the Stark family. Or when bad things happen to good people.'''
	def __init__(self, first_name = None, is_alive = True):
		super().__init__(first_name = first_name, is_alive = is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"
	
	def print_house_words(self):
		print(self.house_words)
	
	def die(self):
		if self.is_alive:
			self.is_alive = False

