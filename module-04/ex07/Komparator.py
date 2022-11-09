from FileLoader import FileLoader
import sys

class Komparator:
	def __init__(self, df):
		if not isinstance(df, pd.DataFrame):
			sys.exit("Error: cannot initialize Komparator bc df is not a dataframe")
		if df.empty:
			sys.exit("Error: cannot initialize Komparator bc df is empty")
		self.df = df
	
		def compare_box_plots(self, categorical_var, numerical_var):
			pass

		def density(self, categorical_var, numerical_var):
			pass

		def compare_histograms(self, categorical_var, numerical_var):
			pass
