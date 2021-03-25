from python_graphql_client import GraphqlClient

#All methods return a query in graphql to RaM API 
class RaMQuerys():

	def singular_query_maker(self, schema, id, fields):
		"""
		Ask for 'fields' of 'schema['id]' 
		"""
		query = "query{ " + schema + "(id: " + str(id) + "){ "
		for f in fields:
			query += f + " "
		query += "} }"
		return query

	def plural_query_maker(self, schema, page, _filter, fields):
		"""
		Ask for 'fields' of all entries of the 'page' that fullfil '_filter' of 'schema' at RaM API
		page make sense if the answer of "fullfil '_filter' of 'schema'" has more entries that space on
		a respond from the api, otherwise page need to be one
		"""
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
		"""
		Ask for 'fields' of all entries of the 'page' that fullfil '_filter' of 'schema' at RaM API
		page make sense if the answer of "fullfil '_filter' of 'schema'" has more entries that space on
		a respond from the api, otherwise page need to be one
		"""
		query = "query { "+ schema+"ByIds(ids: " + str(ids) + ") { "
		for f in fields:
			query += f + " "
		query += "} }"
		return query

	def first_question_query_mold(self, page, schema, char):
		"""
		Ask for entries that have 'char' (case insensitive) in the names of the 'schema' of RaM API
		"""
		return RaMQuerys.plural_query_maker(self, schema, page, '{ name: "'+ char +'" }', ["name"])

	def forth_query(self, page, view):
		"""
		Ask for the list of origins_ids of all the characters involved in all the episodes
		"""
		query = "query { episodes (page: "+str(page)+"){ info{ pages next }"
		query += " results{ name id characters{ origin{ id "
		if view:
			query += "name "
		query += "} } } } }"
		return query
	
