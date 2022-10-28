kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == "__main__":
	print("module_" + str(kata[0]).zfill(2), ", ex_" + str(kata[1]).zfill(2), sep = '', end = '')
	print(" : " + str(round(kata[2], 2)), end = '')
	print(", " + "{:.2e}".format(kata[3]), end = '')
	print(", " + "{:.2e}".format(kata[4]))

