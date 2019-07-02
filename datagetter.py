import requests
import json

class Retriever(object):
	def __init__(self, entry='', playerid=0):
			self.heroDefaults()
			self.hero = entry
			self.id = playerid
			self.heroID = 0

	def heroDefaults(self):
		with open('heros.json', 'r') as myfile:
			data = myfile.read()
		self.heroValues = json.loads(data)

	def call(self):
		for i in self.heroValues:  # verify the hero name exists
			if len(self.hero) > 1 and self.hero in i['name']:
				self.hero = i['localized_name']
				self.heroID = i['id']
				print('The hero {} exists! It has an ID Number of {}'.format(self.hero, self.heroID))
				break
		with open('current_Stats.json', 'w') as outfile:
			data = requests.get('https://api.opendota.com/api/herostats').content
			loaded = json.loads(data)
			json.dump(loaded, outfile)

t = Retriever('void')
t.call()