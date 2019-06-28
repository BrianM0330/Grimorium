import requests
import json

class Retriever(object):
	def __init__(self, heroname='', playerid=0):
		with open('heros.json', 'r') as myfile:
			data = myfile.read()
			self.hero = heroname
			self.id = playerid
			self.heroIDs = json.loads(data)
			self.api = 'https://api.opendota.com/api/heroes/{}/matches'

	def call(self):
		self.realName = ''
		for i in self.heroIDs:
			if len(self.hero) > 1 and self.hero in i['name']:
				self.realName = i['localized_name']
				print(self.realName)
				break

t = Retriever('void')
t.call()