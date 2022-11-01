from vector import Vector

if __name__ == "__main__":
	v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
	print(v1)
	v2 = v1 * 5
	print(v2)

	print()
	v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
	v2 = v1 * 5
	print(v2)

	print()
	v2 = v1 / 2.0
	print(v2)
	print(v1)

	print()
	v3 = v2 - v1
	print(v3)

	print()
	v3 = v2 + v1
	print(v3)

	print()
	v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
	print(v2.shape)
	print(v2.T())

	print()
	v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
	v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
	print(v1.dot(v2))
