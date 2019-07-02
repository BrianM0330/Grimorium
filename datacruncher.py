import plotly
import pandas
import json

def analyze():
	with open('current_Stats.json') as infile:
		data = json.load(infile)
	for i in data:
		print( i['legs'] )

analyze()