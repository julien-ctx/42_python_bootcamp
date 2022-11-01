import sys
if __name__ == "__main__":
	if len(sys.argv) > 1:
		morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.'
					}
		s = ' '.join(filter(None, sys.argv[1:]))
		if not all(c.isalnum() or c.isspace() for c in s):
			print("ERROR")
			exit(1)
		s = s.upper()
		s = s.replace(' ', '/')
		s = ' '.join(s)
		for c in s:
			tmp = c
			for letter in morse_dict:
				if c == letter:
					tmp = morse_dict[letter]
					break
			print(tmp, end = "")
		print()
