from datagetter import Retriever
import plotly.graph_objects as go
import numpy as np
import json

#go = graph_objects


class Crunchy(Retriever):

	def __init__(self):
		Retriever.__init__(self)
		self.isUtility= False
		self.isFarmer = False
		self.isGanker = False
		
		self.lowHP = False
		self.lowMana = False
		self.lowArmor = False

		self.totalPicks = 0
		self.totalWins = 0

		self.call()
		with open('recent_stats.json') as infile:
			self.data = json.load(infile)
		with open ('hero_benchmarks.json') as infile2:
			self.benchmark_data = json.load(infile2)

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

	def get_benchmarks(self):
		gpm_percentile99 = 0
		gpm_percentile50 = 0
		gpm_percentile10 = 0
		gpm_totals = []
		gpm_stdev = 0

		lh10_percentile99 = 0
		lh10_percentile50 = 0
		lh10_percentile10 = 0
		lh10_totals = []
		lh10_stdev = 0

		for i in self.benchmark_data['result']['gold_per_min']:
			gpm_stdev = np.std(gpm_totals)

			if i['percentile'] == 0.1:
				gpm_percentile10 = i['value']
				gpm_totals.append(i['value'])

			if i['percentile'] == 0.2:
				gpm_totals.append(i['value'])
			if i['percentile'] == 0.3:
				gpm_totals.append(i['value'])
			if i['percentile'] == 0.4:
				gpm_totals.append(i['value'])
			if i['percentile'] == 0.5:
				gpm_percentile50 = i['value']
				gpm_totals.append(i['value'])

			if i['percentile'] == 0.6:
				gpm_totals.append(i['value'])
			if i['percentile'] == 0.7:
				gpm_totals.append(i['value'])
			if i['percentile'] == 0.8:
				gpm_totals.append(i['value'])
			if i['percentile'] == 0.9:
				gpm_totals.append(i['value'])
			if i['percentile'] == 0.95:
				gpm_totals.append(i['value'])
			if i['percentile'] == 0.99:
				gpm_percentile99 = i['value']
				gpm_totals.append(i['value'])

		print("On average expect to get a GPM of {}. On a good game {} and on a bad one {}".format(gpm_percentile50, gpm_percentile99, gpm_percentile10))
		print("There is a standard deviation of {}".format(gpm_stdev))

	def graph(self):
		range = np.arange(10)

		fig = go.Figure(data=go.Scatter(x=range, y=range**2))

		fig.show()

t = Crunchy()
t.call()
t.win_rates()
t.get_benchmarks()
t.graph()