import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://www.tutorialspoint.com/selenium/practice/text-box.php"
driver.get(url)
driver.maximize_window()
time.sleep(2)

form = driver.find_element(By.ID, "headingTwo")
form.click()
time.sleep(2)

practice_form = driver.find_element(By.XPATH, "//a[@href='selenium_automation_practice.php']")
practice_form.click()
time.sleep(2)

genders = driver.find_elements(By.XPATH, "//div[@class='d-flex justify-content-start align-center']")
for gender in genders:
    print(gender.text)

male_gender = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"gender")))
male_gender.click()

hobbies = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"hobbies")))
hobbies.click()
time.sleep(2)
driver.quit()