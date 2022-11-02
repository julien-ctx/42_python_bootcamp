import sys

class Evaluator:
	@staticmethod
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		if not (isinstance(coefs, list) and isinstance(words, list)):
			sys.exit("Bad argument types in .zip_evaluate")
		if not all(isinstance(x, str) for x in words):
			sys.exit("Words list can only contain strings")
		if not all(isinstance(x, float) for x in coefs):
			sys.exit("Coefs list can only contain floats")
		total = 0.0
		for x, y in zip(words, coefs):
			total += len(x) * y
		return total

	@staticmethod
	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		if not (isinstance(coefs, list) and isinstance(words, list)):
			sys.exit("Bad argument types in .enumerate_evaluate")
		if not all(isinstance(x, str) for x in words):
			sys.exit("Words list can only contain strings")
		if not all(isinstance(x, float) for x in coefs):
			sys.exit("Coefs list can only contain floats")
		total = 0.0
		for x in enumerate(words):
			total += len(x[1]) * coefs[x[0]]
		return total
		

if __name__ == "__main__":
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))

	words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
	coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))

	coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42, 1.0]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))
