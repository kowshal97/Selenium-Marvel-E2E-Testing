import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://training.openspan.com/login"
driver.get(url)
driver.maximize_window()
time.sleep(2)

submit = driver.find_element(By.ID,"login_button").is_enabled()
print(submit)
time.sleep(2)

element1 = driver.find_element(By.ID,"user_name").send_keys("leodas")
element2 = driver.find_element(By.ID,"user_pass").send_keys("leodasd11w313")

submit2 = driver.find_element(By.ID,"login_button").is_enabled()
print(submit2)
time.sleep(2)
driver.quit()