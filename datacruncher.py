import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from datagetter import Retriever
import json


class Crunchy(Retriever):

	def analyze(self):
		with open('current_Stats.json') as infile:
			data = json.load(infile)
		for i in data:
			name = i['localized_name']
			legCount = i['legs']
			winRate1 = i['1_win'] / i['1_pick']
			print( name + '\t' +  str(legCount)+ '\t'  + str(winRate1) )

	# plot( [ {'x': [1,2,3], 'y': [3,1,6]    }   ]   )

t = Crunchy('Axe')