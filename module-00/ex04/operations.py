import sys
import decimal

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

if __name__ == "__main__":
	if len(sys.argv) == 1 or len(sys.argv) == 2:
		print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
	else:
		assert len(sys.argv) == 3, "too many arguments"
		assert check_int(sys.argv[1]) and check_int(sys.argv[2]), "only integers"
		print("Sum:", int(sys.argv[1]) + int(sys.argv[2]), sep='\t\t')
		print("Difference:", int(sys.argv[1]) - int(sys.argv[2]), sep='\t')
		print("Product:", int(sys.argv[1]) * int(sys.argv[2]), sep='\t')
		if not int(sys.argv[2]):
			print("Quotient:", "ERROR (division by zero)", sep='\t')
			print("Remainder:", "ERROR (modulo by zero)", sep='\t')
		else:
			print("Quotient:", round(int(sys.argv[1]) / int(sys.argv[2]), 4), sep='\t')
			print("Remainder:", int(sys.argv[1]) % int(sys.argv[2]), sep='\t')

