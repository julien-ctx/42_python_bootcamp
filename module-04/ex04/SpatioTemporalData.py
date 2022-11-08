from FileLoader import FileLoader

class SpatioTemporalData:

	def __init__(self, df):
		self.df = df
	
	def when(self, location):
		dates = []
		d = self.df[self.df.City == location]
		if d.empty:
			return []
		[dates.append(getattr(row, "Year")) for row in d.itertuples() if getattr(row, "Year") not in dates]
		return dates

	def where(self, date):
		d = self.df[self.df.Year == date]
		if d.empty:
			return None
		return [d["City"].iloc[0]]

loader = FileLoader()
data = loader.load("athlete_events.csv")
sp = SpatioTemporalData(data)
print(sp.when('Athina'))
print()
print(sp.when('Paris'))
print()
print(sp.where(1896))
print()
print(sp.where(2016))
