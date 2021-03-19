

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

	def duplicate_elimination_by_origin_id(self, original):
		ids = []
		for i in original:
			if i['origin']['id'] not in ids:
				ids.append(i['origin']['id'])
		return ids
