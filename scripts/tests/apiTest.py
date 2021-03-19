from django.test import TestCase

#ram => Rick and Morty
class ApiTest(TestCase):

	def test_ram_graphql_connection(self):
		"""
		test the most basic example of ram graphql
		"""
		self.assertEquals(False, True)