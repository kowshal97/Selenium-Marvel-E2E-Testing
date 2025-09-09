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
url = "https://qa-automation-practice.netlify.app/radiobuttons"
driver.get(url)
driver.maximize_window()
time.sleep(2)

radio1 = driver.find_element(By.ID, "radio-button1").click()
print(driver.find_element(By.ID, "radio-button1").is_selected())
time.sleep(2)

radio2 = driver.find_element(By.ID, "radio-button2").click()
print(driver.find_element(By.ID, "radio-button2").is_selected())
time.sleep(2)

radio3 = driver.find_element(By.ID, "radio-button3").click()
print(driver.find_element(By.ID, "radio-button3").is_selected())
time.sleep(2)

radio4 = driver.find_element(By.ID, "radio-button4").click()
print(driver.find_element(By.ID, "radio-button4").is_selected())
time.sleep(2)
driver.quit()