import unittest


class Test(unittest.TestCase):
	def test_firstTest(self):
		print("this is my first unit test case")




if __name__=="__main__":
	unittest.main()

"""




import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time


logging.basicConfig(filename= "test.log",
	format= '%(asctime)s: %(l)'
	level=logging.DEBUG
	)
logging.debug("this is a debug message")
logging.info("this is a info message")
logging.warning("this is a warning message") #printed
logging.error("this is a error message") #printed
logging.critical("this is a critical message") #printed




"""
