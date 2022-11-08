from FileLoader import FileLoader

def youngest_fellah(df, year):
	loader = FileLoader()
	if df is not None:
		return {'f': df[(df.Year == year) & (df.Sex == "F")]["Age"].min(), \
				 'm': df[(df.Year == year) & (df.Sex == "M")]["Age"].min()}
	else:
		return None


loader = FileLoader()
data = loader.load("athlete_events.csv")
print(youngest_fellah(data, 2004))
