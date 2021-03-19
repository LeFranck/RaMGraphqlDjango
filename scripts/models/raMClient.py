from python_graphql_client import GraphqlClient

# Create your models here.
class RaMClient():
	endpoint = "https://rickandmortyapi.com/graphql" 
	client = GraphqlClient(endpoint=endpoint)

	def get_ram_graphql_connection(self):
		query_rick = RaMClient.singular_query_maker(self, "character", 1, ["name"])
		return self.client.execute(query=query_rick)

	def singular_query_maker(self, schema, id, fields):
		query = "query{ " + schema + "(id: " + str(id) + "){ "
		for f in fields:
			query += f + " "
		query += "} }"
		return query

	def plural_query_maker(self, schema, page, _filter, fields):
		query = "query{ " + schema
		if page != "" and _filter != "":
			query += "(page: " + str(page) + ", filter: " + _filter + ")"
		elif page == "" and _filter != "":
			query += "(filter: " + _filter + ")"
		elif page != "" and _filter == "":
			query += "(page: " + str(page) + ")"
		else:
			query += ""
		query += "{ info { next pages } results { "
		for f in fields:
			query += f + " "
		query += "} } }"
		return query

	def first_query(self):
		return RaMClient.plural_query_maker(self, "locations", 1, '{ name: "l" }', ["name"])

	def second_query(self):
		return RaMClient.plural_query_maker(self, "episodes", 1, '{ name: "e" }', ["name"])

	def third_query(self):
		return RaMClient.plural_query_maker(self, "characters", 1, '{ name: "c" }', ["name"])

