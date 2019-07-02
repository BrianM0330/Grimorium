import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import json

def analyze():
	with open('current_Stats.json') as infile:
		data = json.load(infile)
	for i in data:
		name = i['localized_name']
		legCount = i['legs']
		winRate1 = i['1_win'] / i['1_pick']
		print( name + '\t' +  str(legCount)+ '\t'  + str(winRate1) )

analyze()