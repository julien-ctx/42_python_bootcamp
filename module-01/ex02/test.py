from vector import Vector

if __name__ == "__main__":
	v1 = Vector([[1.0], [1.0], [3.0]])
	v2 = Vector([[4.0], [1.0], [6.0]])
	# v3 = v2 * v1
	# print(str(v3.values))
	v3 = v2 / v1
	print(str(v3.values))
