
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time



driver = webdriver.Chrome()
driver.get("file:///home/string/Desktop/selenium_ide/SDET/table.html")

rows = len(driver.find_elements(By.XPATH,"/html/body/table/tbody/tr"))
cols = len(driver.find_elements(By.XPATH,"/html/body/table/tbody/tr[1]/th"))
#print(len(elems))

for r in range(2,rows+1):
	for c in range(1,cols+1):
		s1=  str(r)
		s2 = str(c)
		string = "/html/body/table/tbody/tr["+ s1 +"]/td["+ s2 +"]"
		value = driver.find_element(By.XPATH,string).text
		print(value)


"""

print(driver.current_window_handle)

handles = driver.window_handles


for han in handles:
	driver.switch_to.window(han)
	print(driver.title)


driver.quit()
"""

"""driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame") # first frame
time.sleep(2)
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(2)
driver.switch_to.default_content()
time.sleep(2)
driver.switch_to.frame("packageFrame") # sec frame
time.sleep(2)
driver.find_element(By.LINK_TEXT, "WebDriver").click()"""


#driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
#time.sleep(5)
#driver.switch_to_alert().accept()
#driver.switch_to_alert().dismiss()
#
