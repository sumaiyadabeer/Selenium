
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
from selenium.webdriver import ActionChains



driver = webdriver.Chrome()
#driver.maximize_window()

driver.get("https://www.amazon.in")

cookies = driver.get_cookies() #dictionary of all cookies
print(len(cookies))
print(cookies)

#adding new cookie on the browser
cookie = {'name': 'Mycookie', 'value' : '123456789'}
driver.add_cookie(cookie)

cookies = driver.get_cookies() 
print(len(cookies))
#print("after adding cookie" + str(cookies)    # why this is acting strangely    one ) is missing LOL




#deleting a cookie
driver.delete_cookie('Mycookie')  
#driver.delete_cookie('Mycookie')
cookies = driver.get_cookies() 
print(len(cookies))
#print("after deleting the cookie" + str(cookies)



#delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies() #dictionary of all cookies
print(len(cookies))
print(cookies)




"""sou = driver.find_element(By.XPATH, "//*[@id='box6']")
tar = driver.find_element(By.XPATH, "//*[@id='box106']")


actions= ActionChains(driver)
actions.drag_and_drop(sou , tar).perform()
"""

"""

print(driver.current_window_handle)

handles = driver.window_handles

rows = len(driver.find_elements(By.XPATH,"/html/body/table/tbody/tr"))
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
