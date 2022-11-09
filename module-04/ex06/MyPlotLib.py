#https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114
from FileLoader import FileLoader
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import scipy

class MyPlotLib:
	
	def histogram(self, df, features):
		fig = plt.figure()
		for i, feature in enumerate(features):
			ax = fig.add_subplot(1, len(features) ,i + 1)
			df[feature].hist(bins=10,ax=ax)
			ax.set_title(feature)
		fig.tight_layout()
		plt.show()

	def density(self, df, features):
		for feature in features:
			df[feature].plot.density()
			plt.legend(feature)
		plt.show()

	def pair_plot(self, df, features):
		if len(features) != 2:
			print("Error: pairplot must have a pair of values")
			return
		sns.pairplot(df, vars=[features[0], features[1]])
		plt.show()
		pass

	def box_plot(self, df, features):
		pass

loader = FileLoader()
plot = MyPlotLib()
data = loader.load("athlete_events.csv")
# plot.histogram(data, ["Height", "Weight"])
plot.density(data, ["Height", "Weight"])
# plot.pair_plot(data, ["Weight", "Height"])
