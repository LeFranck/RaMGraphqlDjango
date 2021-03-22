from python_graphql_client import GraphqlClient
import aiohttp
import asyncio
import async_timeout
import time

from . import RaMQuerys
from . import RaMStats

class RaMClient():
	endpoint = "https://rickandmortyapi.com/graphql"
	client = GraphqlClient(endpoint=endpoint)

	def get_ram_graphql_connection(self):
		"""
		Simple query to RaM API using Graphql
		"""
		query_rick = RaMQuerys.singular_query_maker(RaMQuerys, "character", 1, ["name"])
		return self.client.execute(query=query_rick)

	async def char_query(self, loop, schema, char, client):
		"""
		How many times 'char' (case insensitive) appears in the names of all the 'schema' of RaM API
		"""
		page = "1"
		cont_total = 0
		query = RaMQuerys.first_question_query_mold(RaMQuerys, page, schema, char)
		page = RaMClient.client.execute(query)

		nextPage = page['data'][schema]['info']['next']
		pages = page['data'][schema]['info']['pages']
		to_count = page['data'][schema]['results']
		cont_total += RaMStats.char_count(RaMStats, to_count, char)

		tasks = []
		for i in range(nextPage, pages + 1):
			query_i = RaMQuerys.first_question_query_mold(RaMQuerys, i , schema, char)
			tasks.append(client.execute_async(query_i))
		tasks_results = await asyncio.gather(*tasks)

		for j in tasks_results:
			cont_total += RaMStats.char_count(RaMStats, j['data'][schema]['results'], char)
		return cont_total

	async def first_round(self, loop):
		"""
		How many times 'l' (case insensitive) appears in the names of all the 'locations' of RaM API
		How many times 'e' (case insensitive) appears in the names of all the 'episodes' of RaM API
		How many times 'c' (case insensitive) appears in the names of all the 'characters' of RaM API
		"""
		client = GraphqlClient(endpoint=self.endpoint,loop=loop)
		tasks = []
		tasks.append(RaMClient.char_query(self, loop, "locations", "l", client))
		tasks.append(RaMClient.char_query(self, loop, "episodes", "e", client))
		tasks.append(RaMClient.char_query(self, loop, "characters", "c", client))
		retorno = await asyncio.gather(*tasks)
		return retorno

	async def second_round(self, loop):
		"""
		returns a dictionary, with episode_id as key, and as value have a pair of data,
		the first entry its how many diferent origins have all the characters involved in
		that episode, and the second entry its the list of origins_ids of all the characters 
		involved in that episode (without repetition)
		"""
		query = RaMQuerys.forth_query(RaMQuerys, "1")
		page = RaMClient.client.execute(query)
		Pages = page['data']['episodes']['info']['pages']

		client = GraphqlClient(endpoint=self.endpoint,loop=loop)
		tasks = []
		for i in range(1, Pages + 1):
			query_i = RaMQuerys.forth_query(RaMQuerys,i)
			tasks.append(client.execute_async(query_i))
		aps = await asyncio.gather(*tasks)

		episode_origins_dict = {}
		for j in aps:
			for episode in j['data']['episodes']['results']:
				Id = episode['id']
				characters = episode['characters']
				origins = RaMStats.duplicate_elimination_by_origin_id(RaMStats, characters)
				episode_origins_dict[Id] = origins

		return RaMStats.second_round_output(RaMStats, episode_origins_dict)

	def run_first_round(self):
		"""
		Runs first_round and time it
		"""
		starttime = time.time()
		loop = asyncio.get_event_loop()
		retorno = loop.run_until_complete(RaMClient.first_round(self, loop))
		duration = time.time() - starttime
		return retorno, duration

	def run_second_round(self):
		"""
		Runs second_round and time it
		"""
		starttime = time.time()
		loop = asyncio.get_event_loop()
		# hola = loop.run_until_complete(RaMClient.char_query(self, loop, "locations", "l"))
		retorno = loop.run_until_complete(RaMClient.second_round(self, loop))
		duration = time.time() - starttime
		return retorno, duration
