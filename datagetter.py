import requests
import json

class Retriever(object):
    def __init__(self, heroname='', playerid = 0):
        self.hero = heroname
        self.id = playerid
        self.heroIDs = {'antimage': 1, 'axe': 2, 'bane': 3, 'bloodseeker': 4, 'crystalmaiden': 5, 'drow': 6,
                        'earth shaker': 7, 'juggernaut': 8, 'mirana': 9, 'nevermore': 10, 'morphling': 11,
                        'phantom lancer': 12, 'puck': 13, 'pudge': 14, 'razor': 15, 'sand_king': 16, 'storm': 17,
                        'sven': 18, 'tiny': 19, 'vengeful spirit': 20, 'windrunner': 21, 'zeus': 22, 'kunkka': 23,
                        'lina': 24, 'lich': 25, 'lion': 26, 'shadow shaman': 27, 'slardar': 28, 'tidehunter': 29,
                        'witch doctor': 30, 'riki': 31, 'enigma': 32, 'tinker': 33, 'sniper': 34, 'necro': 35,
                        'warlock': 36, 'beastmaster': 37, 'queen of pain': 38, 'veno': 39, 'faceless void': 40,
                        'wraith king': 41, 'death prophet': 42, 'phantom assassin': 43, 'pugna': 44, 'templar': 45,
                        'viper': 46, 'luna': 47, 'dragon knight': 48, 'dazzle': 49, 'clockwork': 50, 'leshrac': 51,
                        'natures prophet': 52, 'furion': 52, 'lifestealer': 53, 'naix': 53, 'dark seer': 54,
                        'clinkz': 55, 'omniknight': 56, 'enchantress': 57, 'ench': 57, 'huskar': 58,
                        'night stalker': 59,
                        'balanar': 59, 'brood': 60, 'broodmother': 60, 'bounty hunter': 61, 'gondar': 61, 'weaver': 62,
                        'nerubian weaver': 62, 'jakiro': 63, 'batrider': 64, 'chen': 65, 'spectre': 66, 'spec': 66,
                        'doom': 67, 'ancient apparition': 68, 'aa': 68, 'ursa': 69, 'ulsafaar': 69,
                        'spirit breaker': 70,
                        'sb': 70, 'barathrum': 70, 'gyrocopter': 71, 'gyro': 71, 'alchemist': 72, 'invoker': 74,
                        'silencer': 75, 'outworld devourer': 76, 'lycan': 77, 'brewmaster': 78, 'shadow deomon': 79,
                        'lone druid': 80, 'chaos knight': 81, 'meepo': 82, 'treant': 83, 'ogre magi': 84, 'undying': 85,
                        'rubick': 86, 'nyx': 87, 'naga siren': 88, 'keeper of the light': 89, 'wisp': 90, 'visage': 91,
                        'slark': 92, 'medusa': 93, 'troll warlord': 94, 'centaur': 95, 'magnus': 96, 'timbersaw': 97,
                        'bristleback': 98, 'tusk': 99, 'skywrath': 100, 'abaddon': 100, 'elder_titan': 101,
                        'legion commander': 102, 'ember spirit': 103, 'earth spirit': 104, 'underlord': 105,
                        'terrorblade': 106, 'phoenix': 107, 'techies': 108, 'oracle': 109, 'wyvern': 110,
                        'arc warden': 111,
                        'monkey king': 112, 'dark willow': 113, 'grimstroke': 114, 'mars': 115}

    def call(self):
        api = 'https://api.opendota.com/api/recentMatches=
