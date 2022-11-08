from FileLoader import FileLoader

def proportion_by_sport(df, year, sport, gender):
	if df.empty:
		return None
	df = df[(df.Sex == gender) & (df.Year == year)].drop_duplicates(subset=["Name"], keep="first")
	total = len(df)
	return len(df[(df.Sex == gender) & (df.Sport == sport) & (df.Year == year)]) / total

loader = FileLoader()
data = loader.load("athlete_events.csv")
print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
