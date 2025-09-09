import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#step1 launching browser
driver = webdriver.Chrome()

#step2 element control for python/ Navigate browser
driver.get("https://concertcraze.netlify.app/")
driver.maximize_window()
time.sleep(2)

#step3
Hamburger = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "hamburger")))
Hamburger.click()
login_link = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "loginLink")))
login_link.click()

#step4 interacting with sign up button
signup = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/html/signup']"))
)
signup.click()
print("signup button clicked sucessfully")
time.sleep(2)

#step5
username = driver.find_element(By.ID, "username")
username.send_keys("leodas1")

email = driver.find_element(By.ID, "email")
test_email = f"leodas+{uuid.uuid4().hex[:6]}@gmail.com"
email.send_keys(test_email)
print(test_email)

password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, "password")))
password.send_keys("Gymfreek@123")
confirm_password = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH , "//*[@id='confirm-password']")))
confirm_password.send_keys("Gymfreek@123")

signup_submit = driver.find_element(By.XPATH, "//*[@id='signup-form']/button")
signup_submit.click()
print("signup button clicked sucessfully")
time.sleep(2)

WebDriverWait(driver,10).until(EC.url_changes(driver.current_url))
time.sleep(2)