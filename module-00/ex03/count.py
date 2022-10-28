import string
import sys

def text_analyzer(s = None):
	'''
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	'''
	if s is None:
		print("What is the text to analyze?")
		return
	assert isinstance(s, str), "argument is not a string"
	print("The text contains", sum(1 for c in s), "character(s):")
	print("-", sum(1 for c in s if c.isupper()), "upper letter(s)")
	print("-", sum(1 for c in s if c.islower()), "lower letter(s)")
	print("-", sum(1 for c in s if c in string.punctuation), "punctuation mark(s)")
	print("-", sum(1 for c in s if c.isspace()), "space(s)")

if (__name__ == "__main__"):
	if len(sys.argv) != 2:
		print("Error: please provide one argument")
	else:
		text_analyzer(sys.argv[1])
