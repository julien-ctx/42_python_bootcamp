import random

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

if __name__ == "__main__":
	print("This is an interactive guessing game!")
	print("You have to enter a number between 1 and 99 to find out the secret number.")
	print("Type 'exit' to end the game.")
	print("Good luck!\n")
	to_guess = random.randint(1, 99)
	usr_input = ''
	count = 1
	while not usr_input:
		usr_input = input("What's your guess between 1 and 99?\n>> ")
		if usr_input:
			if usr_input == 'exit':
				print("Goodbye!")
				exit(1)
			if check_int(usr_input):
				if int(usr_input) > 99 or int(usr_input) < 1:
					print("Your number is out of range!")
					usr_input = ''
				else:
					if int(usr_input) > to_guess:
						print("Too high!")
						usr_input = ''
						count += 1
					elif int(usr_input) < to_guess:
						print("Too low!")
						usr_input = ''
						count += 1
					else:
						if to_guess == 42:
							print("The answer to the ultimate question of life, the universe and everything is 42.")
						if count == 1:
							print("Congratulations! You got it on your first try!")
						else:
							print("Congratulations, you've got it!")
							print("You won in " + str(count) + " attempt(s)")
			else:
				print("That's not a number")
				usr_input = ''
