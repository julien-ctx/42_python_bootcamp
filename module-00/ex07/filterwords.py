import sys
import string

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def get_non_punc(s):
	i = 0
	for c in s:
		if c not in string.punctuation:
			i += 1
	return i

def without_punc(s):
	for c in s:
		if c in string.punctuation:
			s = s.replace(c, '')
	return s

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Please use a correct format: python3 filterwords.py [string] [integer]")
	elif not check_int(sys.argv[2]):
		print("Error: second argument needs to be an integer")
	else:
		if int(sys.argv[2]) < 0:
			print("Please enter a non-negative integer")
			exit(1)
		split = sys.argv[1].split()
		filtered = [without_punc(x) for x in split if get_non_punc(x) > int(sys.argv[2])]
		print(filtered)
