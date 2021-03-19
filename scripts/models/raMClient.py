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

	def query_by_ids_maker(self, schema, ids, fields):
		query = "query { "+ schema+"ByIds(ids: " + str(ids) + ") { "
		for f in fields:
			query += f + " "
		query += "} }"
		return query

	def first_question_query_mold(self, page, schema, char):
		return RaMClient.plural_query_maker(self, schema, page, '{ name: "'+ char +'" }', ["name"])

	def forth_query(self, page):
		query = "query { episodes (page: "+str(page)+"){ info{ pages next }"
		query += " results{ id characters{ origin{ id } } } } }"
		return query