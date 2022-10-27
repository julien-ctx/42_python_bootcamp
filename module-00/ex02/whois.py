import sys

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

if len(sys.argv) == 1:
	exit(1)
assert len(sys.argv) == 2, "more than one argument are provided"
assert check_int(sys.argv[1]), "argument is not an integer"
val = int(sys.argv[1])
if not val:
	print("I'm Zero.")
elif val % 2:
	print("I'm Odd.")
else:
	print("I'm Even")
