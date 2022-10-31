from datetime import datetime
from recipe import Recipe
import string

class Book:
	def getName(self):
		return self.name
	
	def __init__(self, name = "Default book"):
		self.name = name
		self.creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.last_update = self.creation_date
		self.recipes_list = {"starter": [],
							"lunch": [],
							"dessert": []
							}

	def add_recipe(self, recipe):
		if not isinstance(recipe, Recipe):
			print("Error: you can only add recipes to the book")
			return
		for types in self.recipes_list:
			for saved_recipe in self.recipes_list[types]:
				if recipe.getName() == saved_recipe.getName():
					print("Error: this recipe already exists")
					return
		self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.recipes_list[recipe.getType()].append(recipe)

	def get_recipe_by_name(self, name):
		for types in self.recipes_list:
			for recipe in self.recipes_list[types]:
				if name == recipe.getName():
					print(str(recipe))

	def get_recipes_by_types(self, recipe_type):
		names = []
		if not recipe_type == "starter" and not recipe_type == "lunch" and not recipe_type == "dessert":
			print("Error: please enter a valid recipe type")
			return None
		else:
			for recipe in self.recipes_list[recipe_type]:
				names.append(recipe.getName())
			return names
		
	def getLastUpdate(self):
		return self.last_update
