from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

DRIVER_PATH = '/path/to/browser'



# if you want to use chromedriver
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# if you want to use geckodriver
# driver = webdriver.Firefox(executable_path=DRIVER_PATH)


driver.get('https://google.com')