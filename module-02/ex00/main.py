from ft_map import ft_map as ft_map
import string

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96;1m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94;1m'
   GREEN = '\033[92;1m'
   YELLOW = '\033[93m'
   RED = '\033[91;1m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def calculateSquare(n):
    return n * n

if __name__ == "__main__":

	numbers = (1, 2, 3, 4)

	print(color.BOLD + "Map function:" + color.END)
	result = map(calculateSquare, numbers)
	print(set(result))

	print(color.BOLD + "My map function:", color.END)
	result = ft_map(calculateSquare, numbers)
	print(set(result))

	print(color.BOLD + "My map function with a wrong argument:" + color.END)
	ft_map(calculateSquare, 6)

	print(color.BOLD + "Map function with a wrong argument:" + color.END)
	map(calculateSquare, 6)
