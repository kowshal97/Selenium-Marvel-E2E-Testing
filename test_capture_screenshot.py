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
url = "https://seleniumbase.io/demo_page"
driver.get(url)
driver.maximize_window()
time.sleep(2)

element =  driver.find_element(By.TAG_NAME,"h2")
element.screenshot("web.png")
element.screenshot("D://pictures/web2.png")
time.sleep(2)

driver.get_screenshot_as_file(".//web1.png")
time.sleep(2)
driver.get_screenshot_as_file("D://pictures/web2.png")

driver.quit()
