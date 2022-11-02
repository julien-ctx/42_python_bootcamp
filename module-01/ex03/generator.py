import string, random
import sys

def generator(s = None, sep = " ", option = None):
	'''
	Splits the text according to sep value and yield the substrings.
	option precise if a action is performed to the substrings before it is yielded.
	'''
	if not s or not isinstance(s, str):
		sys.exit("Error: check text format")
	if not s.isprintable():
		sys.exit("Error: some characters are not printable.")
	s = s.split(sep)
	if option == "shuffle":
		for item in s:
			rand1 = random.randint(0, len(s) - 1)
			rand2 = random.randint(0, len(s) - 1)
			s[rand1], s[rand2] = s[rand2], s[rand1]
	elif option == "unique":
		s = sorted(set(s), key = s.index)
	elif option == "ordered":
		s.sort()
	elif option: #to check if wrong option is given
		sys.exit("ERROR")
	for item in s:
		yield item


	
if __name__ == "__main__":
	text = "Le Lorem Ipsum est simplement du faux texte."
	for word in generator(text, sep=" "):
		print(word)
	print("\n\033[1m" + "** With ordered option **" + "\033[0m\n")
	for word in generator(text, sep=" ", option="ordered"):
		print(word)

	print("\n\033[1m" + "** With suffle option twice to see the difference" + "\033[0m\n")
	for word in generator(text, sep=" ", option="shuffle"):
		print(word)
	print()
	for word in generator(text, sep=" ", option="shuffle"):
		print(word)

	text = "Salut Bonjour Bonjour Test Test lol Test"
	print("\n\033[1m" + "** With unique option **" + "\033[0m\n")

	for word in generator(text, sep=" ", option="unique"):
		print(word)

	print("\n\033[1m" + "** With wrong option **" + "\033[0m\n")
	for word in generator(text, sep=" ", option="fake"):
		print(word)
