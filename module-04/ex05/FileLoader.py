import pandas as pd
import math

class FileLoader:
	def load(self, path):
		if not isinstance(path, str):
			return None
		try:
			df = pd.read_csv(path)
			print(f"Loaded {len(df)} rows x {len(df.columns)} columns")
			return df
		except Exception as e:
			print(e)

	def display(self, df, n):
		if df is not None:
			if abs(n) > len(df) or n == 0:
				return None
			if n < 0:
				return df.truncate(after=len(df) - abs(n))
			else:
				return df.truncate(before=n)
			return None
		else:
			return None

if __name__ == "__main__":
	fl = FileLoader()
	df = fl.load("good.csv")
	print(fl.display(df, -3))
	print()
	print(fl.display(df, 3))
