from python_graphql_client import GraphqlClient

# Create your models here.
class RaMClient():
	endpoint = "https://rickandmortyapi.com/graphql" 
	client = GraphqlClient(endpoint=endpoint)

	def get_ram_graphql_connection(self):
		query_rick = RaMClient.singular_query_maker(self, "character", 1, ["name"])
		return self.client.execute(query=query_rick)

	def singular_query_maker(self, schema, id, fields):
		query = "query{ " + schema + "(id: " + str(id) + "){"
		for f in fields:
			query += f + " "
		query += "} }"
		return query