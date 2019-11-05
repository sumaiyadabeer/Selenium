
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_dictionary": "/home/string/Downloads/mypath"})


driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
