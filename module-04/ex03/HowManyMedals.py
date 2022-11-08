from FileLoader import FileLoader

def how_many_medals(df, name):
	df = df[df.Name == name].drop(columns = ["ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Season","City","Sport","Event"]).fillna('None')
	dic = {}
	for year, medal in zip(df[['Year']], df[['Medal']]):
		for curr_year, curr_medal in zip(df[year], df[medal]):
			if curr_year not in dic.keys():
				dic[curr_year] = ({'G': 0, 'S': 0, 'B': 0})
			if curr_medal == "Gold":
				dic[curr_year]['G'] += 1
			elif curr_medal == "Silver":
				dic[curr_year]['S'] += 1
			elif curr_medal == "Bronze":
				dic[curr_year]['B'] += 1
	return dic

loader = FileLoader()
data = loader.load('athlete_events.csv')
print(how_many_medals(data, 'Kjetil Andr Aamodt'))
