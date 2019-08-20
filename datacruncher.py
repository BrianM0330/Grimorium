from datagetter import Retriever
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import json
import urls
from bs4 import BeautifulSoup
import requests


class Crunchy(Retriever):

	def __init__(self, entry=''):
		Retriever.__init__(self, entry)
		self.hero = entry.lower()
		self.url = ''
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
				self.data = i  # makes data the hero dictionary
				name = i['localized_name']
				leg_count = i['legs']

				self.winrate_herald = i['1_win'] / i['1_pick']  # herald
				self.pick_totals.append(i['1_pick'])
				self.win_totals.append(i['1_win'])

				self.winrate_guardian = i['2_win'] / i['2_pick']  # guardian
				self.pick_totals.append(i['2_pick'])
				self.win_totals.append(i['2_win'])

				self.winrate_crusader = i['3_win'] / i['3_pick']  # crusader
				self.pick_totals.append(i['3_pick'])
				self.win_totals.append(i['3_win'])

				self.winrate_archon = i['4_win'] / i['4_pick']  # archon
				self.pick_totals.append(i['4_pick'])
				self.win_totals.append(i['4_win'])

				self.winrate_legend = i['5_win'] / i['5_pick']  # legend
				self.pick_totals.append(i['5_pick'])
				self.win_totals.append(i['5_win'])

				self.winrate_ancient = i['6_win'] / i['6_pick']  # ancient
				self.pick_totals.append(i['6_pick'])
				self.win_totals.append(i['6_win'])

				self.winrate_divine = i['7_win'] / i['7_pick']  # divine
				self.pick_totals.append(i['7_pick'])
				self.win_totals.append(i['7_win'])

				self.winrate_pro_league = i['pro_win'] / i['pro_pick']  # pro league
				self.pick_totals.append(i['8_pick'])
				self.win_totals.append(i['8_win'])

				self.totalPicks = sum(self.pick_totals)
				self.totalWins = sum(self.win_totals)
				self.winrate_ratio = self.totalWins / self.totalPicks
				pass

				print(name + '\n' +
				      "This hero has {} legs, let's see how it performs!".format(leg_count) + '\n'

				      + 'Winrate in Herald games:' + '\t' + str(self.winrate_herald) + '\n'

				      + 'Winrate in Guardian games:' + '\t' + str(self.winrate_guardian) + '\n'

				      + 'Winrate in Crusader games:' + '\t' + str(self.winrate_crusader) + '\n'

				      + 'Winrate in Archon games:' + '\t' + str(self.winrate_archon) + '\n'

				      + 'Winrate in Legend games:' + '\t' + str(self.winrate_legend) + '\n'

				      + 'Winrate in Ancient games:' + '\t' + str(self.winrate_ancient) + '\n'

				      + 'Winrate in Divine games:' + '\t' + str(self.winrate_divine) + '\n'

				      + 'Winrate in Pro games games:' + '\t' + str(self.winrate_pro_league) + '\n')

		print("In {} games, {} has an overall winrate of {} ".format(sum(self.pick_totals), self.hero,
		                                                             self.winrate_ratio))
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

		middle_percentile_lh10 = list(self.benchmark_data['result']['lhten'])[4]['value']

		print("On average expect to get a GPM of {}. On a good game {} and on a bad one {}".format(gpm_percentile50,
		                                                                                           gpm_percentile99,
		                                                                                           gpm_percentile10))
		print("There is a standard deviation of {}".format(gpm_stdev))

	def graph(self):
		# --------------------Graphing Hero Picks (Bar)-----------------------------#
		self.data = sorted(self.data.items())  # sorting the json entries
		df = pd.DataFrame.from_dict(self.data, orient='columns')
		df.columns = ['Picks', 'Results']
		df = df.iloc[:16]
		print(df)

		ranks = ['Guardian', 'Crusader', 'Archon', 'Legend', 'Ancient', 'Divine']
		picks = df.iloc[[2, 4, 6, 8, 10, 12], 1]
		wins = df.iloc[[3, 5, 7, 9, 11, 13], 1]

		groupedBar = go.Figure(data=[
			go.Bar(name='Picks', x=ranks, y=picks),
			go.Bar(name='Wins', x=ranks, y=wins)
		])
		groupedBar.update_layout(barmode='group')
		groupedBar.show(renderer='browser')
		# -------------Graphing hero W/L (Line)--------------------------------#
		winrates = [self.winrate_guardian, self.winrate_crusader, self.winrate_archon, self.winrate_legend,
		            self.winrate_ancient, self.winrate_divine]
		lineStats = go.Figure(data=[
			go.Scatter(x=ranks, y=winrates),
			go.Scatter(x=ranks, y=[self.winrate_ratio] * 6)
		]
		)
		lineStats.show(renderer='browser')
		# ---------------------- Subplot -----------------------------#
		fig = make_subplots(rows=1, cols=3)
		fig.add_trace(
			go.Scatter(x=ranks, y=winrates),
			row=1, col=1
		)
		fig.add_trace(
			go.Scatter(x=ranks, y=[self.winrate_ratio] * 6, mode='lines'),
			row=1, col=1
		)
		fig.add_trace(
			go.Bar(name='Picks', x=ranks, y=picks),
			row=1, col=2
		)
		fig.add_trace(
			go.Bar(name='Wins', x=ranks, y=wins),
			row=1, col=3
		)
		fig.add_trace(
			go.Histogram(x=picks, name='test'),
			row=1, col=3
		)
		fig.update_layout(height=800, width=1200, title_text="Test")
		fig.show(renderer='browser')

	def helper(self):
		starting_damage = 0

		# create dataframe for desired values
		df = pd.DataFrame.from_dict(self.data, orient='index')
		df.columns = ['Values']
		df = pd.concat([df.iloc[3:5], df.iloc[8:24]])
		primary_attribute = df.iloc[0][0]

		starting_mana = df.loc['base_mana']['Values'] + (
				df.loc['base_int']['Values'] * 12)  # 12 mana per 1 point of int
		base_stat_low = df.loc['base_attack_min']['Values']
		base_stat_high = df.loc['base_attack_max']['Values']
		# calculations based on the hero's starting values
		if 'Carry' or '2nd_Core' or 'Offlane' in self.roles:  # starting damage only relevant for core heroes
			isCore = True
			if primary_attribute == 'agi':
				base_attribute_bonus = df.loc['base_agi']['Values']
				starting_damage = (base_stat_high + base_stat_low) / 2 + base_attribute_bonus
			elif primary_attribute == 'str':
				base_attribute_bonus = df.loc['base_str']['Values']
				starting_damage = (base_stat_high + base_stat_low) / 2 + base_attribute_bonus
			else:  # int priority 1 hero
				base_attribute_bonus = df.loc['base_int']['Values']
				starting_damage = (base_stat_high + base_stat_low) / 2 + base_attribute_bonus
		# suggestions based on the hero's role and numbers
		if df.loc['attack_type']['Values'] == 'Melee' and starting_damage <= 45 and isCore:
			likes_quelling_blade = True

	def guide_parser(self):
		# looks for hero and its role and matches it to a guide URL
		if 'Carry' in self.roles:
			for key in urls.core_guides:
				if self.hero.lower() in key.lower():
					self.url = urls.core_guides[key]
		elif '2nd_Core' in self.roles:
			for key in urls.core_guides:
				if self.hero.lower() in key.lower():
					self.url = urls.core_guides[key]
		elif 'Support' or '2nd_Supp' or 'Lane_Supp' in self.roles:
			for key in urls.support_guides:
				if self.hero.lower() in key.lower():
					self.url = urls.support_guides[key]
		else: # offlane
			for key in urls.offlane_guides:
				if self.hero.lower() in key.lower():
					self.url = urls.offlane_guides[key]

		suggested_item_phases = []
		suggested_item_names = []

		soup = BeautifulSoup(requests.get(self.url).content, 'html.parser')

		guide_html = requests.get(soup.find("iframe")["src"])
		guide_soup = BeautifulSoup(guide_html.content, 'html.parser')

		item_build_soup = guide_soup.find_all('div', {'class': 'itemBuildContainer'})

		list_index = -1
		for section in item_build_soup:
			list_index += 1
			suggested_item_names.append([])
			suggested_item_phases.append(section.text)
			for i in section.contents[1].contents[1].contents:
				item = i.attrs['itemname']
				suggested_item_names[list_index].append(item)
		suggested_items = dict(zip(suggested_item_phases, suggested_item_names))
		for item in suggested_items:
			print(item, suggested_items[item], end='\n')
		return suggested_items


t = Crunchy('Terrorblade')
t.call()
t.win_rates()
t.get_benchmarks()
# t.graph()
t.helper()
t.guide_parser()
