import time
from random import randint
import os

# https://www.datacamp.com/tutorial/decorators-python

def log(func):
	def timer(*args, **kwargs):
		name = ' '.join(func.__name__.split('_')).title()
		start = time.time()
		res = func(*args, **kwargs)
		end = time.time()
		with open("machine.log", "a+") as f:
			f.write('(' + os.environ['USER'] + ")Running: " + name.ljust(19, ' '))
			timing = (end - start) * 1000
			if timing / 1000 < 1:
				f.write("[ exec-time = " + str(round(timing, 3)) + " ms ]")
			else:
				f.write("[ exec-time = " + str(round(timing / 1000, 3)) + " s ]")
			f.write('\n')
		return res
	return timer

class CoffeeMachine():

	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False
		
	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)
