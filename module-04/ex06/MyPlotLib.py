#https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114
import matplotlib.pyplot as plt
import matplotlib
from FileLoader import FileLoader
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
		fig = plt.figure()
		for feature in features:
			df[feature].plot.density()
			plt.legend(feature)
		fig.tight_layout()
		plt.show()

	def pair_plot(self, df, features):
		pass

	def box_plot(self, df, features):
		pass

loader = FileLoader()
plot = MyPlotLib()
data = loader.load("athlete_events.csv")
plot.histogram(data, ["Height", "Weight"])
plot.density(data, ["Height", "Weight"])
