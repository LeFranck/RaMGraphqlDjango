from django.test import TestCase

class IndexViewTest(TestCase):

	def test_no_api_connetion(self):
		"""
		if it cant connect shuld return a 404 error
		"""
		self.assertEquals(False, True)

	def test_char_counter_format(self):
		"""
		The format of char counter div
		"""
		self.assertEquals(False, True)

	def test_episode_locations_format(self):
		"""
		The format of episode locations div
		"""		
		self.assertEquals(False, True)

	def test_char_counter_execution(self):
		"""
		After cliking run it should display running
		"""		
		self.assertEquals(False, True)

	def test_char_counter_result(self):
		"""
		After getting the result it should display it, with the time it took
		"""		
		self.assertEquals(False, True)
		
	def test_episode_locations_execution(self):
		"""
		After clicking run it should display running
		"""		
		self.assertEquals(False, True)

	def test_episode_locations_result(self):
		"""
		After getting the result it should display it, with the time it took
		"""		
		self.assertEquals(False, True)

		
