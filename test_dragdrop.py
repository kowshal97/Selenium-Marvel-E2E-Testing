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
url = "https://the-internet.herokuapp.com/drag_and_drop"
driver.get(url)
driver.maximize_window()
time.sleep(2)

action = ActionChains(driver)
source = driver.find_element(By.ID, "column-a")
destination = driver.find_element(By.ID, "column-b")
time.sleep(2)
action.drag_and_drop(source, destination).perform()
time.sleep(2)
action.drag_and_drop(destination, source).perform()
driver.quit()