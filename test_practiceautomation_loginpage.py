import time


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(2)

driver.get("https://practicetestautomation.com/practice-test-login/")

user_name = driver.find_element(By.ID, "username")
user_name.send_keys("student")

Password = driver.find_element(By.ID, "password")
Password.send_keys("Password123")

submit = driver.find_element(By.ID, "submit")
submit.click()

loggin_sucess = driver.find_element(By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1")
if loggin_sucess.is_displayed:
    print("Logged In Successfully")
else:
    print("Logged is not Successfully")

time.sleep(2)

