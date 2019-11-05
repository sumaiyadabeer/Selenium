
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time



driver = webdriver.Chrome()
#driver.get("http://newtours.demoaut.com/")
driver.get("https://stage.newsgallery.com/")

links=driver.find_elements(By.TAG_NAME,"a")
#print(type(links))

for link in links:
	print(link.text)





#driver.find_element(By.LINK_TEXT, "REGISTER").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click() # can be first or last

