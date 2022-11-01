import string, random

def generator(s = None, sep = " ", option = None):
	'''
	Splits the text according to sep value and yield the substrings.
	option precise if a action is performed to the substrings before it is yielded.
	'''
	if not s.isprintable():
		print("Error: some characters are not printable.")
	s = s.split(sep)
	if option == "shuffle":
		print("ghnhng")
		for item in s:
			rand1 = random.randint(0, len(s) - 1)
			rand2 = random.randint(0, len(s) - 1)
			s[rand1], s[rand2] = s[rand2], s[rand1]
	elif option == "unique":
		s = sorted(set(s), key = s.index)
	elif option == "ordered":
		s = sorted(s)
	print(s)


	
if __name__ == "__main__":
	generator("calut Vest blol", " ", "ordered")
