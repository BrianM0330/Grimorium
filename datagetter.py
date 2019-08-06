import requests
import json

class Retriever(object):
	"""This class' main purpose is to initialize a hero with the proper attributes. These
	attributes are neceessary for analyzing hero data. It also initializes important JSON
	files containing important values."""
	def __init__(self, entry='', playerid=0):
			self.heroDefaults()
			self.id = playerid
			self.heroID = 0
			self.hero = entry.lower()
			self.roles = []
			if len(self.hero) == 0:
				self.hero = self.promptforHero()

	def heroDefaults(self):
		"""Opens the json file with heredata and loads it into self.heroValues """
		with open('heros.json', 'r') as myfile:
			data = myfile.read()
		self.heroValues = json.loads(data) #need to only get the specific dictionary for the hero

	def promptforHero(self):
		"""A simple prompt used if the entry is blank or a hero doesn't exist"""
		self.hero = input('Could you please enter the hero you want stats for? \n ')
		return self.hero.lower()

	def call(self):
		"""First checks if hero exists. If it does, it then gets its localized_name and id from
		heros.json. It also fixes spaces in the hero name."""
		if ' ' in self.hero:    #before calling for stats, make sure hero will be valid
			self.hero = self.hero.replace(' ', '_')
		if '-' in self.hero:
			self.hero = self.hero.replace('-', '')

		for i in self.heroValues:
			if len(self.hero) > 1 and self.hero in i['name']:
				self.roles = i['roles']
				self.hero = i['localized_name']
				self.heroID = i['id']
				print('The hero {} exists! It has an ID Number of {}'.format(self.hero, self.heroID))
				pass

		#gets daily stats
		with open('recent_stats.json', 'w') as outfile:
			data = requests.get('https://api.opendota.com/api/herostats').content
			loaded = json.loads(data)
			json.dump(loaded, outfile)

		#gets benchmarks
		with open('hero_benchmarks.json', 'w') as outfile:
			benchmarks = requests.get('https://api.opendota.com/api/benchmarks?hero_id={}'.format(self.heroID)).content
			loading = json.loads(benchmarks)
			json.dump(loading, outfile)