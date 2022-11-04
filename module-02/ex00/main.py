from ft_map import ft_map as ft_map
import string

def calculateSquare(n):
    return n * n

if __name__ == "__main__":

	x = [1, 2, 3, 4, 5]
	# next(ft_map(calculateSquare, None)) # to check that error management works
	# next(None, x)) # to check that error management works
	print(ft_map(lambda dum: dum + 1, x))
	print(list(ft_map(lambda dum: dum + 1, x)))
