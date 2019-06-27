import requests
import json


class Retriever(object):
    def __init__(self, heroname='', playerid = 0):
        with open('heros.json', 'r') as myfile:
            data = myfile.read()

        self.hero = heroname
        self.id = playerid
        self.heroIDs = json.loads(data)

    def call(self):
        api = 'https://api.opendota.com/api/recentMatches='
