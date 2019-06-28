import requests
import json
import time

class Retriever(object):
	def __init__(self, entry='', playerid=0):
		with open('heros.json', 'r') as myfile:
			data = myfile.read()
			self.hero = entry
			self.id = playerid
			self.heroID = 0
			self.heroValues = json.loads(data)
			self.api = 'https://api.opendota.com/api/heroes/{}/matches'

	def recents(self):
		self.api = 'https://api.opendota.com/api/heroes/{}/matches'.format(self.heroID)
		print(self.api)
		request = requests.get(self.api)


	def call(self):
		self.realName = ''
		for i in self.heroValues:  # verify the hero name exists
			if len(self.hero) > 1 and self.hero in i['name']:
				self.hero = i['localized_name']
				self.heroID = i['id']
				print('The hero {} exists! It has an ID Number of {}'.format(self.hero, self.heroID))
				break
		print('Please wait while I find match data on this hero...')
		time.sleep(2)
		self.recents()



t = Retriever('void')
t.call()