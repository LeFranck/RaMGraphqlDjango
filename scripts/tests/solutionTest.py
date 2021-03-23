from django.test import TestCase
from scripts.models import raMStats
from scripts.models import raMClient
import time

class SolutionTest(TestCase):

	def test_char_counter_no_encounter(self):
		"""
		Function should return 0 if there is no coincidence of chars
		"""
		example = [
			{"name": "abcdefg"},
			{"name": "bcdefgh"},
			{"name": "cdefghi"},
		]
		count = raMStats.RaMStats.char_count(raMStats.RaMStats, example, 'x')
		self.assertEquals(0, count)

	def test_char_counter_no_caps(self):
		"""
		Function should return the correct amount of chars when there is no cap
		"""		
		example = [
			{"name": "abcdefg"},
			{"name": "bcdefgh"},
			{"name": "cdefghi"},
		]
		count = raMStats.RaMStats.char_count(raMStats.RaMStats, example, 'd')
		self.assertEquals(3, count)

	def test_char_counter_caps(self):
		"""
		Function should return the correct amount of chars when there is only CAP
		"""		
		example = [
			{"name": "ABCDEFG"},
			{"name": "BCDEFGH"},
			{"name": "CDEFGHI"},
		]
		count = raMStats.RaMStats.char_count(raMStats.RaMStats, example, 'd')
		self.assertEquals(3, count)

	def test_char_counter_mixed(self):
		"""
		Function should return the correct amount of chars when its mixed
		"""		
		example = [
			{"name": "ABCDEFG"},
			{"name": "bcdefgh"},
			{"name": "CDEFGHI"},
		]
		count = raMStats.RaMStats.char_count(raMStats.RaMStats, example, 'd')
		self.assertEquals(3, count)

	def test_list_duplicate_elimination_by_origin_id_empty_list(self):
		"""
		Function should return empty list
		"""
		example = []
		resultado = raMStats.RaMStats.duplicate_elimination_by_origin_id(raMStats.RaMStats, example)
		self.assertEquals([], resultado)
		self.assertEquals(0, len(resultado))

	def test_list_duplicate_elimination_by_origin_id_no_duplicates(self):
		"""
		Function should return same list
		"""
		example = [
			{"origin": {	"id": "1",	} },
			{"origin": {	"id": "2",	}	},
			{"origin": {	"id": "3",	}	},
		]		
		resultado = raMStats.RaMStats.duplicate_elimination_by_origin_id(raMStats.RaMStats, example)
		self.assertEquals(["1","2","3"], resultado)
		self.assertEquals(3, len(resultado))

	def test_list_duplicate_elimination_by_origin_id_diferente_duplicates(self):
		"""
		Function should return list without duplicates
		"""		
		example = [
			{"origin": {	"id": "1",	} },
			{"origin": {	"id": "2",	}	},
			{"origin": {	"id": "2",	}	},
			{"origin": {	"id": "1",	}	},
			{"origin": {	"id": "3",	}	},
		]		
		resultado = raMStats.RaMStats.duplicate_elimination_by_origin_id(raMStats.RaMStats, example)
		self.assertEquals(["1","2","3"], resultado)
		self.assertEquals(3, len(resultado))

	def test_list_duplicate_elimination_by_origin_id_same_duplicate_couple_of_time(self):
		"""
		Function should return list without duplicates
		"""		

		example = [
			{"origin": {	"id": "1",	} },
			{"origin": {	"id": "2",	}	},
			{"origin": {	"id": "2",	}	},
			{"origin": {	"id": "2",	}	},
			{"origin": {	"id": "3",	}	},
		]		
		resultado = raMStats.RaMStats.duplicate_elimination_by_origin_id(raMStats.RaMStats, example)
		self.assertEquals(["1","2","3"], resultado)
		self.assertEquals(3, len(resultado))

	def test_get_time_of_execution(self):
		"""
		Function should calculate correctly time execution
		"""
		starttime = time.time()
		for i in range(3):
			time.sleep(1)
		endtime = time.time()
		t = endtime - starttime
		self.assertGreaterEqual(3.1, t)
		self.assertLessEqual(3, t)

	def test_round_1(self):
		_, duration = raMClient.RaMClient.run_first_round(raMClient.RaMClient)
		self.assertGreaterEqual(4, duration)

	def test_round_2(self):
		_, duration = raMClient.RaMClient.run_second_round(raMClient.RaMClient)
		self.assertGreaterEqual(4, duration)