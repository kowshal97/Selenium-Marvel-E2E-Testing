import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

header = driver.find_element(By.TAG_NAME, "h2").text
print(header)
expected_header = "Test login"

assert header == expected_header, f"text does not match. Expected '{expected_header}', but got '{header}'"
driver.quit()