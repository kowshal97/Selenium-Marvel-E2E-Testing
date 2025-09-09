import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://www.tutorialspoint.com/selenium/practice/text-box.php"
driver.get(url)
driver.maximize_window()
time.sleep(2)


alerts_window = driver.find_element(By.ID, "headingThree")
alerts_window.click()
time.sleep(2)
alerts_tab = driver.find_element(By.XPATH, "//a[@href='alerts.php']")
alerts_tab.click()


alerts1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']"))
)
alerts1.click()
time.sleep(2)
alerts1 = driver.switch_to.alert
time.sleep(2)
alerts1.accept()
time.sleep(2)




alert2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div[2]/div[2]/button"))
)
alert2.click()
time.sleep(6)
alert2 = driver.switch_to.alert
alert2.accept()
time.sleep(5)

alert3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div[3]/button"))
)
alert3.click()
time.sleep(2)
alert3 = driver.switch_to.alert
alert3.dismiss()
time.sleep(2)

alert4 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//html/body/main/div/div/div[2]/div[4]/button"))
)
alert4.click()

prompt_alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
prompt_alert.send_keys("Kowshal")
time.sleep(1)
driver.quit()
