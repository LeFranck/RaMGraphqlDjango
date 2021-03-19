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