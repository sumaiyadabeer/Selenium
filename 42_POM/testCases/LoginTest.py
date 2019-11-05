
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import sys
import time
from LoginPage import LoginPage

sys.path.append("/home/string/Desktop/selenium_ide/SDET/42_POM")

class LoginTest(unittest.TestCase):
	baseURL = "http://admin-demo.nopcommerce.com/"
	username = "admin@yourstore.com"
	password = "admin"
	driver = webdriver.Chrome()

	@classmethod
	def setUpClass(cls):
		cls.driver.get(cls.baseURL)
		cls.driver.maximize_window()



	def test_login(self):
		lp= LoginPage(self.driver)
		lp.setUserName(self.username)
		lp.setPassword(self.password)
		lp.clickLogin()
		time.sleep(5)
		self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "webpage title are not matching")

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()


if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="./reports"))
