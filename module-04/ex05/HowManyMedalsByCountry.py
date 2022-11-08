from FileLoader import FileLoader
import pandas as pd
def how_many_medals_by_country(df, name):
	if df.empty:
		return None
	mask = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby', 'Lacrosse', 'Polo']
	d = df[df.Team == name]
	d = d[d['Sport'].isin(mask)]
	d = d.drop_duplicates(subset=['Sport'])
	d = d.drop(columns = ["ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Season","City","Sport","Event"]).fillna('None').sort_values(by=['Year'])
	if d.empty:
		return None
	dic = {}
	for i in range(0, 2):
		for year, medal in zip(d[['Year']], d[['Medal']]):
			for curr_year, curr_medal in zip(d[year], d[medal]):
				if curr_year not in dic.keys():
					dic[curr_year] = ({'G': 0, 'S': 0, 'B': 0})
				if curr_medal == "Gold":
					dic[curr_year]['G'] += 1
				elif curr_medal == "Silver":
					dic[curr_year]['S'] += 1
				elif curr_medal == "Bronze":
					dic[curr_year]['B'] += 1
		d = df[df.Team == name]
		d = d[~d['Sport'].isin(mask)]
		d = d.drop(columns = ["ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Season","City","Sport","Event"]).fillna('None').sort_values(by=['Year'])
	return dic
	
loader = FileLoader()
data = loader.load("athlete_events.csv")
print(how_many_medals_by_country(data, 'Australia'))
