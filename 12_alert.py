
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time



driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")




driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
#driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()
#
