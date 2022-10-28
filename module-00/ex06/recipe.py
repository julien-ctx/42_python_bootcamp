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

def print_details():
	s = ''
	while not s:
		s = input("Please enter a recipe to print its details:\n>> ")
	assert isinstance(s, str), "argument is not a string"
	for key in cookbook:
		if key == s:
			print("Here are the ingredients of " + key + ":")
			print("- " + "\n- ".join(cookbook[key]["ingredients"]))
			print("It takes " + str(cookbook[key]["prep_time"]) + " minutes to cook this " + cookbook[key]["meal"])
			return
	print("This recipe doesn't exist!")

def delete_recipe():
	s = ''
	while not s:
		s = input("Please enter a recipe to delete it:\n>> ")
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
		for key in cookbook:
			if key == name:
				print("This recipe already exists!")
				return
	print("Enter ingredients:")
	ingredients = []
	while "ingredients":
		single_ing = input()
		if not single_ing and ingredients:
			break
		if not single_ing:
			continue;
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
	cookbook[name] = {"ingredients": ingredients, "meal": meal, "prep_time": time}

if __name__ == "__main__":
	print("Welcome to the Python Cookbook !\nList of available option:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit\n")
	option = ''
	while "recipe":
		while not option:
			option = input("\nPlease select an option:\n>> ")
			if option:
				if not check_int(option):
					print("Please enter an integer value")
					option = ''
		if int(option) == 1:
			add_recipe()		
		elif int(option) == 2:
			delete_recipe()
		elif int(option) == 3:
			print_details()
		elif int(option) == 4:
			print_all()
		elif int(option) == 5:
			print("\nGoodbye!\n")
			exit(0)
		else:
			print("\nSorry, this option does not exist.")
			print("List of available option:")
			print("\t1: Add a recipe")
			print("\t2: Delete a recipe")
			print("\t3: Print a recipe")
			print("\t4: Print the cookbook")
			print("\t5: Quit\n")
		option = ''
