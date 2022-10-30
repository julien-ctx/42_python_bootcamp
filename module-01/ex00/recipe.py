def is_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def check_types(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
	if not isinstance(name, str):
		
	if not isinstance(cooking_lvl, int):

class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if not isinstance(cooking_lvl, int):
			print("ok")
			exit(1)
		if not name:
			print("Error: name is undefined!")
			exit(1)
		self.name = name
		if cooking_lvl < 1 or cooking_lvl > 5:
			print("Error: cooking level is out of range!")
			exit(1)
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

if __name__ == "__main__":
	Cake = Recipe("Cake", "D", 0, 0, 0, 0)
