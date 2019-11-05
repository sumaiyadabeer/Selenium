import unittest
#from selenium import webdriver

class SignupTest(unittest.TestCase):

	def test_signupByEmail(self):
		print("this is signup by email test")
		self.assertTrue(True)


	def test_signupByFacebook(self):
		print("this is signup by facebook test")
		self.assertTrue(True)

	def test_signupByTwitter(self):
		print("this is signup by twitter test")
		self.assertTrue(True)


if __name__== "__main__":
	unittest.main()

