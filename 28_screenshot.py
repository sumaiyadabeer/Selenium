
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time



driver = webdriver.Chrome()
driver.get("http://newtours.demoaut.com/")


driver.save_screenshot("/home/string/Desktop/selenium_ide/SDET/screenshot/home.png")
#driver.get_screeenshot_as_file("/home/string/Desktop/selenium_ide/SDET/screenshot/home2.png") #not working in my case
