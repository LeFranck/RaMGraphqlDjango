from django.test import TestCase
from scripts.models import RaMClient

#ram => Rick and Morty
class ApiTest(TestCase):

	def test_ram_graphql_connection(self):
		"""
		test the most basic example of ram graphql
		"""
		result = RaMClient.get_ram_graphql_connection(RaMClient)
		to_test = result['data']['character']['name']
		self.assertEquals('Rick Sanchez', to_test)

	def test_singular_query_maker(self):
		"""
		test the query maker method correctness
		"""
		result = RaMClient.singular_query_maker(RaMClient, "character", 1, ["name", "id"])
		to_test = "query{ character(id: 1){ name id } }"
		self.assertEquals(result, to_test)

	def test_plural_query_maker(self):
		"""
		test the query maker method correctness
		"""
		result = RaMClient.plural_query_maker(RaMClient, "characters", 1 ,'{ name: "r" }', ["name", "id"])
		to_test = 'query{ characters(page: 1, filter: { name: "r" }){ info { next pages } results { name id } } }'
		self.assertEquals(result, to_test)

	def test_query_by_ids_maker(self):
		"""
		test the query maker method correctness
		"""
		result = RaMClient.query_by_ids_maker(RaMClient, "locations", [1,2,3,4,5] ,["name", "id"])
		to_test = 'query { locationsByIds(ids: [1, 2, 3, 4, 5]) { name id } }'
		self.assertEquals(result, to_test)