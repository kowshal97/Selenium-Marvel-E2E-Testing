import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from test_capture_screenshot import element

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://demo.automationtesting.in/Register.html"
driver.get(url)
driver.maximize_window()
time.sleep(2)

element = driver.find_element(By.ID, "checkbox1").get_attribute("value")
print(element)

hobbies = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for hobby in hobbies:
    print(hobby.get_attribute("value"))

time.sleep(2)
driver.quit()