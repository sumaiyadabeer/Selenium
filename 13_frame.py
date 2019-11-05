
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time



driver = webdriver.Chrome()
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame") # first frame
time.sleep(2)
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(2)
driver.switch_to.default_content()
time.sleep(2)
driver.switch_to.frame("packageFrame") # sec frame
time.sleep(2)
driver.find_element(By.LINK_TEXT, "WebDriver").click()


#driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
#time.sleep(5)
#driver.switch_to_alert().accept()
#driver.switch_to_alert().dismiss()
#
