from book import Book
from recipe import Recipe
from time import sleep

if __name__ == "__main__":
	book = Book("My recipe book")
	print("** Checking creation time **")
	print(book.getLastUpdate())
	print()
	
	print("** ...Sleeping... **")
	sleep(2)
	
	print("** Error management for add_recip method **")
	book.add_recipe("Food")
	print()

	print("** Adding a Kebab to the book **")
	kebab = Recipe("Kebab", 1, 5, ["Salad", "Tomatoes", "Onions", "Meat"], "", "lunch")
	book.add_recipe(kebab)
	print()

	print("** Checking updated time **")
	print(book.getLastUpdate())
	print()

	print("** Adding Tacos to the book **")
	tacos = Recipe("Tacos", 1, 10, ["French fries", "Sauce", "Meat"], "French tacos", "lunch")
	book.add_recipe(tacos)

	print("** Showing all lunch recipes **")
	print(str(book.get_recipes_by_types("lunch")))
	print()

	print("** Showing kebab recipe **")
	book.get_recipe_by_name("Kebab")

