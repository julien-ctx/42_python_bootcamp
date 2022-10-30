import datetime
import recipe

class Book:
	def __init__(self, name = "Default book"):
		if not name:
			print("Error: name is undefined")
			exit(1)
		self.name = name
		self.creation_date = datetime.time()
		self.last_update = self.creation_date
		self.recipes_list = {"starter": [],
							"lunch": [],
							"dessert": []
							}

	def add_recipe(self, recipe):
		self.last_update = datetime.time()
		self.recipes_list[recipe.getType()].append(recipe)
	def get_recipe_by_name(self, name):
		for types in self.recipes_list:
			for recipe in self.recipes_list[types]:
				if name == recipe.getName():
					# return recipe
					print(str(recipe))
	# def get_recipes_by_types(self, recipe_type):

Kebab = recipe.Recipe("Kebab", 1, 4, ["tacos"], "", "lunch")
book = Book("Keb")
book.add_recipe(Kebab)
book.get_recipe_by_name("Kebab")
