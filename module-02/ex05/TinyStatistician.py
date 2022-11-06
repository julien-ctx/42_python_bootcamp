import math

class TinyStatistician:

	def mean(self, x):
		if not x:
			return None
		total = 0
		for i in x:
			total += i
		return float(total / len(x))
	
	def median(self, x):
		if not x:
			return None
		x.sort()
		if len(x) % 2 == 0:
			return float((x[int(len(x) / 2)] + x[int(len(x) / 2 - 1 )]) / 2)
		else:
			return float(x[int((len(x) - 1) / 2)])
		
	def quartiles(self, x):
		if not x:
			return None
		x.sort()
		return [float(x[int(len(x) / 4)]), float(x[int(3 * len(x) / 4)])]
	
	def var(self, x):
		if not x:
			return None
		mean = self.mean(x)
		return sum((val - mean) ** 2 for val in x) / len(x)

	def std(self, x):
		if not x:
			return None
		return float(math.sqrt(self.var(x)))

if __name__ == "__main__":
	tstat = TinyStatistician()
	a = [1, 42, 300, 10, 59]
	print(tstat.mean(a))
	# Expected result: 82.4
	print(tstat.median(a))
	# Expected result: 42.0
	print(tstat.quartiles(a))
	# Expected result: [10.0, 59.0]
	print(tstat.var(a))
	# Expected result: 12279.439999999999
	print(tstat.std(a))
	# Expected result: 110.81263465868862
