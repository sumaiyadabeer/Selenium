
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner


class OrangeHRMTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.maximize_window()

	def test_homePageTitle(self):
		self.driver.get("https://opensource-demo.orangehrmlive.com")
		self.assertEqual("OrangeHRM", self.driver.title, "webpage title not matching !!")

	def test_login(self):
		self.driver.get("https://opensource-demo.orangehrmlive.com")
		self.driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
		self.driver.find_element(By.NAME, "txtPassword").send_keys("admin123")
		self.driver.find_element(By.NAME, "Submit").click()
		self.assertEqual("OrangeHRMM", self.driver.title, "webpage title not matching !!")

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		print("Test Compleated.....")



if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="./Reports"))
