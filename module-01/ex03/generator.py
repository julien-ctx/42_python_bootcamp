import string

def generator(s = None, sep = " ", option = None):
'''
Splits the text according to sep value and yield the substrings.
option precise if a action is performed to the substrings before it is yielded.
'''
	if not s.isprintable():
		print("Error: some characters are not printable.")
	
	
if __name__ == "__main__":
