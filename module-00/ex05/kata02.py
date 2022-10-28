kata = (2019, 9, 25, 3, 30)

if __name__ == "__main__":
	for x in kata[1:3]:
		print(str(x).zfill(2), end = '/')
	print(str(kata[0]).zfill(4), end = ' ')
	print(str(kata[3]).zfill(2), end = ':')
	print(str(kata[4]).zfill(2))

