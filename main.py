from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DRIVER_PATH = 'path/to/driver'


# if you want to use chromedriver
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# if you want to use geckodriver
# driver = webdriver.Firefox(executable_path=DRIVER_PATH)


driver.get('https://google.com')

try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "gLFyf")))
finally:
    driver.quit()
    
    
    
    
    
    
    