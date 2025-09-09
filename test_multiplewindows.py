import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.switch_to.new_window()
driver.get("https://www.saucedemo.com/")
driver.switch_to.new_window()
driver.get("https://www.tutorialspoint.com/")
time.sleep(2)
total_tabs = len(driver.window_handles)
print(total_tabs)
value = driver.window_handles
print(value)
current_tab = driver.current_window_handle
print(current_tab)
first_tab = driver.window_handles[0]
driver.switch_to.window(first_tab)
time.sleep(2)
driver.quit()