import unittest
from selenium import webdriver

class Test(unittest.TestCase):

	def testName(self):
		driver= webdriver.Chrome()
		driver.get("https://www.google.com/")
		titleOfWebPage=driver.title
		#assertTrue I EXPECT IT TO BE TRUE
		self.assertTrue("Google" == titleOfWebPage,"webpage title is not same") 
		#assertFalse I EXPECT IT TO BE FALSE
		self.assertFalse("Google" == titleOfWebPage,"webpage title is not same") 



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
