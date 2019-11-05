import unittest
#from selenium import webdriver

class LoginTest(unittest.TestCase):

	def test_loginByEmail(self):
		print("this is login by email test")
		self.assertTrue(True)


	def test_loginByFacebook(self):
		print("this is login by facebook test")
		self.assertTrue(True)

	def test_loginByTwitter(self):
		print("this is login by twitter test")
		self.assertTrue(True)


if __name__== "__main__":
	unittest.main()

