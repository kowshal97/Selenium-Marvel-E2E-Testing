import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
url = "https://demo.guru99.com/test/simple_context_menu.html"
driver.get(url)
driver.maximize_window()
time.sleep(2)

action = ActionChains(driver)
right_click = driver.find_element(By.XPATH,"//*[@id='authentication']/span")
action.context_click(right_click).perform()
time.sleep(2)

context_menu = driver.find_elements(By.XPATH,"//*[@id='authentication']/ul")
for context_menu_element in context_menu:
    print(context_menu_element.text)

driver.quit()