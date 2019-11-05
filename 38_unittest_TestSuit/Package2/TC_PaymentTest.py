import unittest
#from selenium import webdriver

class PaymentTest(unittest.TestCase):

	def test_paymentIndoller(self):
		print("this is payment in doller test")
		self.assertTrue(True)

	def test_paymentInrupees(self):
		print("this is payment in rupees test")
		self.assertTrue(True)


if __name__== "__main__":
	unittest.main()
