from django.test import TestCase
from scripts.models import RaMStats
from scripts.models import RaMClient
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
		count = RaMStats.char_count(RaMStats, example, 'x')
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
		count = RaMStats.char_count(RaMStats, example, 'd')
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
		count = RaMStats.char_count(RaMStats, example, 'd')
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
		count = RaMStats.char_count(RaMStats, example, 'd')
		self.assertEquals(3, count)

	def test_list_duplicate_elimination_by_origin_id_empty_list(self):
		"""
		Function should return empty list
		"""
		example = []
		resultado = RaMStats.duplicate_elimination_by_origin_id(RaMStats, example, False)
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
		resultado = RaMStats.duplicate_elimination_by_origin_id(RaMStats, example, False)
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
		resultado = RaMStats.duplicate_elimination_by_origin_id(RaMStats, example, False)
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
		resultado = RaMStats.duplicate_elimination_by_origin_id(RaMStats, example, False)
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
		"""
		Test how much time round_1 takes to completion (should be less than 4sec)
		"""
		_, duration = RaMClient.run_first_round_console(RaMClient)
		self.assertGreaterEqual(4, duration)

	def test_round_2(self):
		"""
		Test how much time round_2 takes to completion (should be less than 4sec)
		"""
		_, duration = RaMClient.run_second_round_console(RaMClient)
		self.assertGreaterEqual(4, duration)
