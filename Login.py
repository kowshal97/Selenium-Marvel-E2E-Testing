import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#MAKES BROWSER STAYS OPEN
options = Options()
options.add_experimental_option("detach", True)   # 👈 keeps browser open
driver = webdriver.Chrome(options=options)


driver.get("https://concertcraze.netlify.app/index.html")
driver.maximize_window()
time.sleep(1)


hamburger = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'hamburger')))
hamburger.click()

loginlink = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'loginLink')))
loginlink.click()

login_email = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'email')))
login_email.send_keys("leodas+346272@gmail.com")

login_password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'password')))
login_password.send_keys("Gymfreek@123")

login_button = driver.find_element(By.XPATH , "//*[@id='login-form']/button")
login_button.click()
time.sleep(5)

try:
    searchbox = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'searchBox')))
    print("Login successful, search bar available")
except:
    print("Login may have failed (search bar not found)")

# Step 5: Search for "Anirudh"
searchbox.send_keys("Anirudh")

submit_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'searchBtn'))).click()
print("[INFO] Search submitted")

time.sleep(3)
print(" Script finished, browser will stay open")