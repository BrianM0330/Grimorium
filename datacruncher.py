import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from datagetter import Retriever
import json


class Crunchy(Retriever):

	def analyze(self):
		with open('current_Stats.json') as infile:
			data = json.load(infile)
		for i in data:
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


	# plot( [ {'x': [1,2,3], 'y': [3,1,6]    }   ]   )

t = Crunchy('Axe')
t.call()
t.analyze()