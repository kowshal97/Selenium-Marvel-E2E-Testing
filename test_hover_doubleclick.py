import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://demo.guru99.com/test/simple_context_menu.html"
driver.get(url)
driver.maximize_window()
time.sleep(2)


actions = ActionChains(driver)
double_click = driver.find_element(By.XPATH,"//*[@id='authentication']/button")
actions.double_click(double_click).perform()
time.sleep(2)
driver.switch_to.alert.accept()
driver.quit()