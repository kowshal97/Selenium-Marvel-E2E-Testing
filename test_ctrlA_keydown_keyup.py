import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://www.saucedemo.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

actions = ActionChains(driver)
username = driver.find_element(By.ID,"user-name")
username.send_keys("captain")
actions.click(username).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(2)
username.clear()
time.sleep(2)
username.send_keys("loki")
time.sleep(2)
driver.quit()

