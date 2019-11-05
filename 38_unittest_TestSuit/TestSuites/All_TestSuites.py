#donotrun
import unittest
from Package1.TC_LoginTest import LoginTest 
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturns import PaymentReturnsTest

#get all the test from each n every class.
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

sanityTestSuite = unittest.TestSuite([tc1,tc2]) #sanity test suit.
unittest.TextTestRunner().run(sanityTestSuite) 






"""class Test(unittest.TestCase):

	def testName(self):



if __name__== "__main__":
	unittest.main()






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
