import time 

class RaMStats():

	def char_count(self, _list, char):
		"""
		Recibes a list of dictionaries and returns how many times char was on the value 
		asociated with the name key of each dictionary 
		"""
		cont = 0
		for i in _list:
			cont += i["name"].count(char.upper())
			cont += i["name"].count(char.lower())
		return cont

	def duplicate_elimination_by_origin_id(self, original, view):
		"""
		Recibes a list of dictionaries that contains the origin of each character of an
		episode, and returns the same dictionary, but deleting the repetitions of 
		origins ids for each episode
		"""
		ids = []
		names = []
		for i in original:
			if i['origin']['id'] not in ids:
				ids.append(i['origin']['id'])
				if view:
					names.append(i['origin']['name'])
		if view:
			return names
		else:
			return ids

	def second_round_output(self, ram_dict):
		"""
		Recieve a dictionary with keys as episode_id and values as the list of diferents
		origins that the charaters of that episode have. And returns a new dictionary that
		adds the count of that list next to the same list 
		"""
		result = {}
		for key in ram_dict:
			result[key] = [len(ram_dict[key]), ram_dict[key]]
		return result