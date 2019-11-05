import unittest


#setup method : execute before every method actual test method. prerequesite for every method
#teardown method: mutiple time after completion of every test method. 

#setupclass and teardow class: only ONCE before starting of all test classes.

#setumodule and teardown module: before module is started or end.. just one time... always defined outside of class.

def setUpModule():
	print("setUpModule")

def tearDownModule():
	print("tearDownModule")



class AppTesting(unittest.TestCase):
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



	def test_search(self):
		print("this is test search ")

	def test_advancesearch(self):
		print("this is test advance search ")

	def test_prepaidRecharge(self):
		print("this is test prepaid Recharge ")

	def test_postpaidRecharge(self):
		print("this is test postpaid Recharge ")


if __name__=="__main__":
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


"""
