from . import RaMClient
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

	def duplicate_elimination_by_origin_id(self, original):
		ids = []
		for i in original:
			if i['origin']['id'] not in ids:
				ids.append(i['origin']['id'])
		return ids

	def first_question_mold(self, page, schema, char):
		cont_total = 0
		nextPage = page
		while nextPage:
			query = RaMClient.first_question_query_mold(RaMClient, nextPage, schema, char)
			page = RaMClient.client.execute(query)
			nextPage = page['data'][schema]['info']['next']
			to_count = page['data'][schema]['results']
			cont_total += RaMStats.char_count(self, to_count, char)
		return cont_total

	def first_question(self):
		return RaMStats.first_question_mold(self, "1", "locations", "l")

	def second_question(self):
		return RaMStats.first_question_mold(self, "1", "episodes", "e")

	def third_question(self):
		return RaMStats.first_question_mold(self, "1", "characters", "c")

	def first_round_sync(self):
		starttime = time.time()
		results = []
		results.append(RaMStats.first_question(self))
		results.append(RaMStats.second_question(self))
		results.append(RaMStats.third_question(self))
		endtime = time.time()
		total_time = endtime - starttime
		results.append(total_time)
		return results
	
	def second_round_get_dict_sync(self):
		pageNum = "1"
		query = RaMClient.forth_query(RaMClient, pageNum)
		nextPage = pageNum
		final_dict = {}
		while nextPage:
			query = RaMClient.forth_query(RaMClient, nextPage)
			page = RaMClient.client.execute(query)
			nextPage = page['data']['episodes']['info']['next']
			results = page['data']['episodes']['results']
			for episode in results:
				Id = episode['id']
				characters = episode['characters']
				origins = RaMStats.duplicate_elimination_by_origin_id(RaMStats, characters)
				final_dict[Id] = origins

		return final_dict
	
	def second_round_output(self, sync):
		if sync:
			starttime = time.time()
			result = {}
			episode_origins_dict = RaMStats.second_round_get_dict_sync(self)
			for key in episode_origins_dict:
				result[key] = [len(episode_origins_dict[key]), episode_origins_dict[key]]
			endtime = time.time()
			total_time = endtime - starttime
			print("total time: " + str(total_time))
			return result