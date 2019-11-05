import unittest
#from selenium import webdriver

class Test(unittest.TestCase):

	def testName(self):


		#assertGreater
		#assertGreaterEqual
		#assertLess
		#assertLessEqual

		self.assertGreater(100,10)
		self.assertLess(10,100)
		self.assertGreaterEqual(100,100)
		self.assertLessEqual(10,10)


if __name__== "__main__":
	unittest.main()



"""


class SearchEnginesTest(unittest.TestCase):
	def test_Google(self):
		self.driver= webdriver.Chrome()
		self.driver.get("https://www.google.com/")
		print("title of page is "+self.driver.title)
		self.driver.close()


	def test_bing(self):
		self.driver= webdriver.Chrome()
		self.driver.get("https://www.bing.com/")
		print("title of page is "+self.driver.title)
		self.driver.close()
	@classmethod
	def setUp(self):
		print("this is login test")

	@classmethod
	def tearDown(self):
		print("this is logout test\n")

	@classmethod
	def setUpClass(cls):
		print("open application")

	@classmethod
	def tearDownClass(cls):
		print("close app")



"""
