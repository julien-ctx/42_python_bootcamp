class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if not name:
			print("Error: name is undefined")
			exit(1)
		self.name = name
		if cooking_lvl < 1 or cooking_lvl > 5:
			print("Error: cooking level is out of range!")
			exit(1)
		self.cooking_lvl = cooking_lvl
		if cooking_time < 0:
			print("Error: cooking time cannot be negative")
			exit(1)
		self.cooking_time = cooking_time
		if not len(ingredients):
			print("Error: a recipe must have ingredients!")
			exit(1)
		self.ingredients = ingredients
		self.description = description
		if not recipe_type == "starter" and not recipe_type == "lunch" and not recipe_type == "dessert":
			print("Error: recipe type must be starter, lunch or dessert")
			exit(1)
		self.recipe_type = recipe_type
		
	def __str__(self):
		txt = 'Recipe(name="' + self.name + '", cooking_lvl=' + str(self.cooking_lvl)
		txt += ', ingredients=["'
		txt += '", "'.join(self.ingredients)
		txt += '"], '
		if self.description:
			txt += 'description="' + self.description + '", '
		txt += 'recipe_type="' + self.recipe_type+ '")'
		return txt

	def getType(self):
		return self.recipe_type

	def getName(self):
		return self.name

if __name__ == "__main__":
	tourte = Recipe("Tourte", 2, 40, ["Pomme de terre", "Creme", "Pate"], "Greasy but tasty", "lunch")
	to_print = str(tourte)
	print(to_print)
