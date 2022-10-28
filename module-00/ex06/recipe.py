import string
import sys

cookbook = {
	"Sandwich": {	"ingredients": ["ham", "bread", "cheese", "tomatoes"],
					"meal": "lunch",
					"prep_time": 10,
				},
	"Cake": 	{	"ingredients": ["flour", "sugar", "eggs"],
					"meal": "dessert",
					"prep_time": 60,
				},
	"Salad": 	{	"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
					"meal": "lunch",
					"prep_time": 15,
				},
}

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def print_all():
	print("Here's the list of all available recipes:")
	for key in cookbook:
		print("- " + key)

def print_details(s = None):
	if s == None:
		print("Please enter a recipe name");
	else:
		assert isinstance(s, str), "argument is not a string"
		for key in cookbook:
			if key == s:
				print("Here are the ingredients of " + key + ":")
				print("- " + "\n- ".join(cookbook[key]["ingredients"]))
				print("It takes " + str(cookbook[key]["prep_time"]) + " minutes to cook this " + cookbook[key]["meal"])
				return
		print("This recipe doesn't exist!")

def delete_recipe(s = None):
	if s == None:
		print("Please enter a recipe name");
	else:
		assert isinstance(s, str), "argument is not a string"
		for key in cookbook:
			if key == s:
				del cookbook[key]
				return
		print("This recipe doesn't exist!")

def add_recipe():
	name = ''
	while not name:
		name = input("Enter the recipe name: ")
	print("Enter ingredients:")
	ingredients = []
	while "ingredients":
		single_ing = input()
		if not single_ing and ingredients:
			break
		else:
			ingredients.append(single_ing)
	meal = ''	
	while not meal:
		meal = input("Enter a meal type: ")
	time = ''
	while not time:
		time = input("Enter a preparation time: ")
		if time:
			if check_int(time):
				if int(time) < 0:
					print("Please enter a non negative integer")
					time = ''
			else:
				print("Please enter an integer value")
				time = ''
	print(ingredients)
	cookbook[name] = {"ingredients": ingredients, "meal": meal, "prep_time": time}
