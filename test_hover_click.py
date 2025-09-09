import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://practice.expandtesting.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)


actions = ActionChains(driver)
hover_click = driver.find_element(By.XPATH,"//a[@class='btn btn-primary py-sm-2 px-sm-3 rounded-pill me-3']")
actions.click(hover_click).perform()
time.sleep(2)


