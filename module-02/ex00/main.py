from ft_map import ft_map as ft_map
from ft_filter import ft_filter as ft_filter
from ft_reduce import ft_reduce as ft_reduce
import string
from functools import reduce

def calculateSquare(n):
    return n * n

if __name__ == "__main__":

	x = [1, 2, 3, 4, 5]
	# next(ft_map(calculateSquare, None)) # to check that error management works
	# next(None, x)) # to check that error management works
	print(ft_map(lambda dum: dum + 1, x))
	print(list(ft_map(lambda dum: dum + 1, x)))

	print(ft_filter(lambda dum: not (dum % 2), x))
	print(list(ft_filter(lambda dum: not (dum % 2), x)))

	lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
	ft_reduce(lambda u, v: u + v, lst)

	lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
	print(str(ft_reduce(lambda u, v: u + v, lst)))
