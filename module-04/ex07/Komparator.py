from FileLoader import FileLoader
from MyPlotLib import MyPlotLib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys

class Komparator:
	def __init__(self, df):
		if not isinstance(df, pd.DataFrame):
			sys.exit("Error: cannot initialize Komparator bc df is not a dataframe")
		if df.empty:
			sys.exit("Error: cannot initialize Komparator bc df is empty")
		self.df = df
	
	def compare_box_plots(self, categorical_var, numerical_var):
		if categorical_var == 'Name':
			print("Using name as categorical variable is not relevant")
			return
		df = self.df.drop_duplicates(subset=['Name'], keep='first')
		l = df[categorical_var].nunique()
		all_cat = []
		fig = plt.figure()
		i = 0
		for cat in df[categorical_var]:
			if cat not in all_cat:
				i += 1
				all_cat.append(cat)
				ax = fig.add_subplot(1, l, i)
				tmp = df[df[categorical_var] == cat]
				plt.title(cat)
				tmp.boxplot(column=numerical_var)
		plt.show()

	def density(self, categorical_var, numerical_var):
		pass

	def compare_histograms(self, categorical_var, numerical_var):
		pass

loader = FileLoader()
data = loader.load("athlete_events.csv")
komp = Komparator(data)
komp.compare_box_plots('Sex', 'Height')
