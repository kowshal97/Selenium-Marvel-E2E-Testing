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
url = "https://demo.guru99.com/V1/index.php"
driver.get(url)
driver.maximize_window()
time.sleep(2)

bank = driver.find_element(By.PARTIAL_LINK_TEXT,"Bank Project")
bank.click()
time.sleep(2)
driver.quit()