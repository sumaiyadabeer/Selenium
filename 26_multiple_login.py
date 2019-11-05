import XLUTIL
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

path = "/home/string/Desktop/selenium_ide/SDET/Data.xlsx"


rows = XLUTIL.getRowCount(path, "Sheet1")

print(rows)
for r in range(2,6):
	username = XLUTIL.readData(path, "Sheet1", r,1)
	password = XLUTIL.readData(path, "Sheet1", r,2)
	driver.find_element(By.NAME,"userName").send_keys(username)
	driver.find_element(By.NAME,"password").send_keys(password)
	driver.find_element(By.NAME,"login").click()

	if driver.title == "Find a Flight: Mercury Tours:":
		print("test is passed")
		XLUTIL.writeData(path, "Sheet1", r,3,"PASSED")
	else:
		print("test is failed")
		XLUTIL.writeData(path, "Sheet1", r,3,"FAILED")

	driver.find_element(By.LINK_TEXT, "Home").click()





	