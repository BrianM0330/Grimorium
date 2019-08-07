from datagetter import Retriever
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import json


class Crunchy(Retriever):

	def __init__(self, entry=''):
		Retriever.__init__(self, entry)
		self.hero = entry.lower()
		self.isUtility= False
		self.isFarmer = False
		self.isGanker = False

		self.lowHP = False
		self.lowMana = False
		self.lowArmor = False

		self.pick_totals = []
		self.win_totals = []
		self.gpm_totals = []

		self.winrate_guardian = 0
		self.winrate_crusader = 0
		self.winrate_archon = 0
		self.winrate_legend = 0
		self.winrate_ancient = 0
		self.winrate_divine = 0
		self.winrate_ratio = 0

		self.call()
		with open('recent_stats.json') as infile:
			self.data = json.load(infile)
		with open('hero_benchmarks.json') as infile2:
			self.benchmark_data = json.load(infile2)

	def win_rates(self):

		for i in self.data:
			if self.heroID == i['id']:
				self.data = i #makes data the hero dictionary
				name = i['localized_name']
				legCount = i['legs']

				self.winrate_herald = i['1_win'] / i['1_pick']     # herald
				self.pick_totals.append( i['1_pick'] )
				self.win_totals.append( i['1_win'])

				self.winrate_guardian = i['2_win'] / i['2_pick']     # guardian
				self.pick_totals.append( i['2_pick'] )
				self.win_totals.append( i['2_win'])

				self.winrate_crusader = i['3_win'] / i['3_pick']     # crusader
				self.pick_totals.append( i['3_pick'] )
				self.win_totals.append( i['3_win'])

				self.winrate_archon = i['4_win'] / i['4_pick']     # archon
				self.pick_totals.append( i['4_pick'] )
				self.win_totals.append( i['4_win'])

				self.winrate_legend = i['5_win'] / i['5_pick']     # legend
				self.pick_totals.append( i['5_pick'] )
				self.win_totals.append( i['5_win'])

				self.winrate_ancient = i['6_win'] / i['6_pick']     # ancient
				self.pick_totals.append( i['6_pick'] )
				self.win_totals.append( i['6_win'])

				self.winrate_divine = i['7_win'] / i['7_pick']     # divine
				self.pick_totals.append( i['7_pick'] )
				self.win_totals.append( i['7_win'])

				self.winrate_pro_league = i['pro_win'] / i['pro_pick']  # pro league
				self.pick_totals.append( i['8_pick'] )
				self.win_totals.append( i['8_win'])

				self.totalPicks = sum(self.pick_totals)
				self.totalWins = sum(self.win_totals)
				self.winrate_ratio = self.totalWins/self.totalPicks
				pass

				print( name + '\n' +
				       "This hero has {} legs, let's see how it performs!".format(legCount) + '\n'

				       + 'Winrate in Herald games:' + '\t' + str(self.winrate_herald) + '\n'

				       + 'Winrate in Guardian games:' + '\t' + str(self.winrate_guardian) + '\n'

				       + 'Winrate in Crusader games:' + '\t' + str(self.winrate_crusader) + '\n'

				       + 'Winrate in Archon games:' + '\t' + str(self.winrate_archon) + '\n'

				       + 'Winrate in Legend games:' + '\t' + str(self.winrate_legend) + '\n'

				       + 'Winrate in Ancient games:' + '\t' + str(self.winrate_ancient) + '\n'

				       + 'Winrate in Divine games:' + '\t' + str(self.winrate_divine) + '\n'

				       + 'Winrate in Pro games games:' + '\t' + str(self.winrate_pro_league)  + '\n'   )

		print("In {} games, {} has an overall winrate of {} ".format(sum(self.pick_totals), self.hero, self.winrate_ratio))
		pass

	def get_benchmarks(self):
		gpm_percentile99 = 0
		gpm_percentile50 = 0
		gpm_percentile10 = 0
		self.gpm_totals = []
		gpm_stdev = 0

		lh10_percentile99 = 0
		lh10_percentile50 = 0
		lh10_percentile10 = 0
		lh10_totals = []
		lh10_stdev = 0

		for i in self.benchmark_data['result']['gold_per_min']:
			gpm_stdev = np.std(self.gpm_totals)

			if i['percentile'] == 0.1:
				gpm_percentile10 = i['value']
				self.gpm_totals.append(i['value'])

			if i['percentile'] == 0.2:
				self.gpm_totals.append(i['value'])
			if i['percentile'] == 0.3:
				self.gpm_totals.append(i['value'])
			if i['percentile'] == 0.4:
				self.gpm_totals.append(i['value'])
			if i['percentile'] == 0.5:
				gpm_percentile50 = i['value']
				self.gpm_totals.append(i['value'])

			if i['percentile'] == 0.6:
				self.gpm_totals.append(i['value'])
			if i['percentile'] == 0.7:
				self.gpm_totals.append(i['value'])
			if i['percentile'] == 0.8:
				self.gpm_totals.append(i['value'])
			if i['percentile'] == 0.9:
				self.gpm_totals.append(i['value'])
			if i['percentile'] == 0.95:
				self.gpm_totals.append(i['value'])
			if i['percentile'] == 0.99:
				gpm_percentile99 = i['value']
				self.gpm_totals.append(i['value'])

		print("On average expect to get a GPM of {}. On a good game {} and on a bad one {}".format(gpm_percentile50, gpm_percentile99, gpm_percentile10))
		print("There is a standard deviation of {}".format(gpm_stdev))

	def graph(self):
		# --------------------Graphing Hero Picks (Bar)-----------------------------#
		self.data = sorted(self.data.items())  # sorting the json entries
		df = pd.DataFrame.from_dict(self.data, orient='columns')
		df.columns = ['Picks', 'Results']
		df = df.iloc[:16]
		print(df)

		ranks = ['Guardian', 'Crusader', 'Archon', 'Legend', 'Ancient', 'Divine']
		groupedBar = go.Figure(data=[
			go.Bar(name='Picks', x=ranks, y=df.iloc[[2, 4, 6, 8, 10, 12], 1]),
			go.Bar(name='Wins', x=ranks, y=df.iloc[[3, 5, 7, 9, 11, 13], 1])
		])
		groupedBar.update_layout(barmode='group')
		groupedBar.show(renderer='browser')
		# -------------Graphing hero W/L (Line)--------------------------------#
		winrates = [self.winrate_guardian, self.winrate_crusader, self.winrate_archon, self.winrate_legend, self.winrate_ancient, self.winrate_divine]
		lineStats = go.Figure(data=[
		                      go.Scatter(x=ranks, y=winrates),
		                      go.Scatter(x=ranks, y=[self.winrate_ratio]*6)
		                      ]
		                      )
		lineStats.show(renderer='browser')
t = Crunchy('Meepo')
t.call()
t.win_rates()
t.get_benchmarks()
t.graph()