import unittest


class AppTesting(unittest.TestCase):

	@unittest.SkipTest #decorator
	def test_search(self):
		print("this is test search ")

	@unittest.skip("reason: I am skippng this test method bcz this is no ready yet")
	def test_advancesearch(self):
		print("this is test advance search ")

	@unittest.skipIf(1==1, "this is my message")
	def test_prepaidRecharge(self):
		print("this is test prepaid Recharge ")

	def test_postpaidRecharge(self):
		print("this is test postpaid Recharge ")

	def test_loginbygmail(self):
		print("this is test login by gmail")

	def test_loginbytwitter(self):
		print("this is test login by twitter")


if __name__== "__main__":
	unittest.main()



"""
from selenium import webdriver

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
