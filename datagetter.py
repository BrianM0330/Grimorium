import requests
import json

class Retriever(object):
	def __init__(self, entry='', playerid=0):
			self.heroDefaults()
			self.id = playerid
			self.heroID = 0
			self.hero = entry.lower()
			if len(self.hero) == 0:
				self.hero = self.promptforHero()

	def heroDefaults(self):
		"""Opens the json file with heredata and loads it into self.heroValues """
		with open('heros.json', 'r') as myfile:
			data = myfile.read()
		self.heroValues = json.loads(data)

	def promptforHero(self):
		"""A simple prompt used if the entry is blank or a hero doesn't exist"""
		self.hero = input('Hello! Could you please enter the hero you want stats for? \n ')
		return self.hero.lower()

	def call(self):
		"""First checks if hero exists. If it does, it then gets its localized_name and id from
		heros.json. It also fixes spaces in the hero name."""
		if ' ' in self.hero:    #before calling for stats, make sure hero will be valid
			self.hero = self.hero.replace(' ', '_')

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