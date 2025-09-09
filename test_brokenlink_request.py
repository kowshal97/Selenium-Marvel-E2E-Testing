import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url= "https://jqueryui.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)


links = driver.find_elements(By.TAG_NAME,"a")
total_links = len(links)
print(f"Total links: {total_links}")
time.sleep(2)

for link in links:
    href = link.get_attribute("href")

    if href:
        try:
            response = requests.get(href,timeout=5)
            if response.status_code >= 400:
                print(f"Broken Link: {href} (status code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {href}: {e}")

driver.close()