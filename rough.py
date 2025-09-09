import time
from selenium import webdriver
from selenium.webdriver.common.devtools.v137.dom import get_attributes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from Login import searchbox

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://www.marvel.com/games"
driver.get(url)
driver.maximize_window()
time.sleep(2)

searchbox = driver.find_element(By.ID,"search")
searchbox.click()
time.sleep(2)
search_box2 = driver.find_element(By.XPATH,"//input[@placeholder='Search']")
search_box2.send_keys("deadpool")
time.sleep(2)

