import time
from ssl import Options

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://practice.expandtesting.com/hovers"
driver.get(url)
driver.maximize_window()
time.sleep(2)

actions = ActionChains(driver)
hover = driver.find_element(By.XPATH,"//*[@id='core']/div/div/div[1]/img")
actions.move_to_element(hover).perform()
print("step1: ok")
time.sleep(2)

hover1 = driver.find_element(By.XPATH,"//*[@id='core']/div/div/div[2]/img")
actions.move_to_element(hover1).perform()
print("step2: ok")
time.sleep(2)

hover2 = driver.find_element(By.XPATH,"//*[@id='core']/div/div/div[3]/img")
actions.move_to_element(hover2).perform()
print("step3: ok")
time.sleep(2)
driver.quit()