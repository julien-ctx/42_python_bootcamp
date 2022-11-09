#https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114
from FileLoader import FileLoader
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import seaborn as sns
import scipy

class MyPlotLib:
	
	def histogram(self, df, features):
		if not isinstance(df, pd.DataFrame):
			sys.exit("Error: cannot initialize Komparator bc df is not a dataframe")
		if df.empty:
			sys.exit("Error: cannot initialize Komparator bc df is empty")
		fig = plt.figure()
		df = df.drop_duplicates(subset=['Name'], keep='first')
		for i, feature in enumerate(features):
			ax = fig.add_subplot(1, len(features), i + 1)
			df[feature].hist(bins=10,ax=ax)
			ax.set_title(feature)
		fig.tight_layout()
		plt.show()

	def density(self, df, features):
		if not isinstance(df, pd.DataFrame):
			sys.exit("Error: cannot initialize Komparator bc df is not a dataframe")
		if df.empty:
			sys.exit("Error: cannot initialize Komparator bc df is empty")
		df = df.drop_duplicates(subset=['Name'], keep='first')
		for feature in features:
			df[feature].plot.density()
			plt.legend(feature)
		plt.show()

	def pair_plot(self, df, features):
		if not isinstance(df, pd.DataFrame):
			sys.exit("Error: cannot initialize Komparator bc df is not a dataframe")
		if df.empty:
			sys.exit("Error: cannot initialize Komparator bc df is empty")
		if len(features) != 2:
			print("Error: pairplot must have a pair of values")
			return
		df = df.drop_duplicates(subset=['Name'], keep='first')
		sns.pairplot(df, vars=[features[0], features[1]])
		plt.show()
		pass

	def box_plot(self, df, features):
		if not isinstance(df, pd.DataFrame):
			sys.exit("Error: cannot initialize Komparator bc df is not a dataframe")
		if df.empty:
			sys.exit("Error: cannot initialize Komparator bc df is empty")
		df = df.drop_duplicates(subset=['Name'], keep='first')
		df.boxplot(column=features)  
		plt.show()
		pass

loader = FileLoader()
plot = MyPlotLib()
data = loader.load("athlete_events.csv")
# plot.histogram(data, ["Height", "Weight"])
# plot.density(data, ["Height", "Weight"])
# plot.pair_plot(data, ["Weight", "Height"])
# plot.box_plot(data, ["Weight", "Height"])
