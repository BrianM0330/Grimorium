# import plotly.graph_objs as go
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from datagetter import Retriever
import json

class Crunchy(Retriever):

	def __init__(self):
		Retriever.__init__(self)
		self.totalPicks = 0
		self.totalWins = 0
		with open('recent_stats.json') as infile:
			self.data = json.load(infile)
		with open ('hero_benchmarks.json') as infile2:
			self.benchmark_data = json.load(infile2)

	# def totals(self):
	# 	for i in self.data:
	# 		if self.heroID == i['id']:
	# 			self.totalPicks =  i['1_pick'] + i['2_pick']  + i['3_pick']  + i['4_pick']  + i['5_pick']  + i['6_pick'] + i['7_pick']
	# 			self.totalWins = i[]

	def win_rates(self):
		for i in self.data:
			if self.heroID == i['id']:
				name = i['localized_name']
				legCount = i['legs']
				winRate1 = i['1_win'] / i['1_pick']     # herald
				winRate2 = i['2_win'] / i['2_pick']     # guardian
				winRate3 = i['3_win'] / i['3_pick']     # crusader
				winRate4 = i['4_win'] / i['4_pick']     # archon
				winRate5 = i['5_win'] / i['5_pick']     # legend
				winRate6 = i['6_win'] / i['6_pick']     # ancient
				winRate7 = i['7_win'] / i['7_pick']     # divine
				winRate8 = i['pro_win'] / i['pro_pick']     #pro league
				self.totalPicks =  i['1_pick'] + i['2_pick']  + i['3_pick']  + i['4_pick']  + i['5_pick']  + i['6_pick'] + i['7_pick']
				self.totalWins = i['1_win'] + i['2_win'] + i['3_win'] + i['4_win'] + i['5_win'] + i['6_win'] + i['7_win']


				print( name + '\n' +
				       "This hero has {} legs, let's see how it performs!".format(legCount) + '\n'

				       + 'Winrate in Herald games:' + '\t' + str(winRate1) + '\n'

				       + 'Winrate in Guardian games:' + '\t' + str(winRate2) + '\n'

				       + 'Winrate in Crusader games:' + '\t' + str(winRate3) + '\n'

				       + 'Winrate in Archon games:' + '\t' + str(winRate4) + '\n'

				       + 'Winrate in Legend games:' + '\t' + str(winRate5) + '\n'

				       + 'Winrate in Ancient games:' + '\t' + str(winRate6) + '\n'

				       + 'Winrate in Divine games:' + '\t' + str(winRate7) + '\n'

				       + 'Winrate in Pro games games:' + '\t' + str(winRate8)  + '\n'   )

		print("In {} games, {} has an overall winrate of {} ".format(self.totalPicks, self.hero, self.totalWins/self.totalPicks))

	def benchmarks(self):
		for i in self.benchmark_data:
			print(i)
# plot( [ {'x': [1,2,3], 'y': [3,1,6]    }   ]   )

t = Crunchy()
t.call()
t.win_rates()

print( t.benchmark_data )