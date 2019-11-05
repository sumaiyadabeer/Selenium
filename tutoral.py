
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time

def login(uname, pword, driver):
	driver.get("https://stage.newsgallery.com/")

	username = driver.find_element_by_id("guest-login-button").send_keys("\n")

	passw = driver.find_element_by_name("password")
	print(passw)
	passw.send_keys(pword)

	username = driver.find_element_by_id("id_username")
	username.send_keys(uname)

	submit = driver.find_element_by_id("login_button")
	submit.click()







#global driver
driver = webdriver.Chrome()
login("shad", "123456", driver)
t#ime.sleep(10)
#driver.get("https://stage.newsgallery.com/")
#driver.get("https://stage.newsgallery.com/profile/shad/")
#profile_pic = driver.find_element_by_id("user-profile-pic").click()

#driver.close()"""



"""
#driver.maximize_window()
elem = driver.find_element_by_name("session[password]")
elem.clear()
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
sleep(delay)"""




"""import time
import urllib.request
import tarfile
import zipfile

driver_url = "https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz"
driver_filename = driver_url.split("/")[-1]
urllib.request.urlretrieve(driver_url, driver_filename)
archive = tarfile.open(driver_filename)
archive.extractall()
archive.close()

"""

"""from selenium import webdriver
#from  selenium.webdriver.common.keys import keys
from selenium import *
import selenium, time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.google.com/")

print(browser.find_element_by_name("btnI").click())
#browser.get(elem.get_attribute('href'))

#browser.exit()"""

"""import time
from selenium import webdriver

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
print(search_box)
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()"""
