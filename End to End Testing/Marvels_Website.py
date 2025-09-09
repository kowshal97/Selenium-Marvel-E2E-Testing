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

def wait_and_click(driver,locator,timeout=15):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    element.click()


def wait_and_click_send_keys(driver,locator,keys,timeout=15):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    element.clear()
    element.send_keys(keys)

#step2
try:
    url = "https://www.marvel.com/comics"
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)

#step3
    actions = ActionChains(driver)
    element_to_hover = driver.find_element(By.XPATH, "//a[@id='mvl-flyout-button-1']")
    actions.move_to_element(element_to_hover).perform()
    actions.click(element_to_hover).perform()
    print("Hover is successful")
    time.sleep(2)

    element_to_hover2 = driver.find_element(By.XPATH, "//a[@id='mvl-flyout-button-2']")
    actions.move_to_element(element_to_hover2).perform()
    actions.click(element_to_hover2).perform()
    print("Hover2 is successful")
    time.sleep(2)

    element_to_hover3 = driver.find_element(By.XPATH, "//a[@id='mvl-flyout-button-3']")
    actions.move_to_element(element_to_hover3).perform()
    actions.click(element_to_hover3).perform()

    driver.execute_script("window.scrollBy(0,1000);")
    print("Scroll is successful")

#step4
    movie_link = (By.XPATH, "//div[2]//div[1]//div[1]//div[1]//div[1]//div[1]//div[4]//div[1]//div[1]//a[1]//div[1]//div[1]//div[1]//img[1]")
    wait_and_click(driver, movie_link)
    time.sleep(2)
    print("Switched to Movie page")

#step5

    get_now = (By.XPATH,"//span[normalize-space()='Get It Now']")
    wait_and_click(driver, get_now)
    time.sleep(2)
    print("Switched to get now page")

#step5
    get_movie = (By.XPATH,"//img[@alt='Deadpool 2 Movie Poster']")
    wait_and_click(driver, get_movie)
    time.sleep(2)
    print("Switched to deadpool 2 page")

#step5
    stream_page = (By.XPATH,"//span[normalize-space()='Stream on Disney+']")
    wait_and_click(driver, stream_page)
    time.sleep(2)
    print("Switched to stream on disney page")


    time.sleep(2)
    driver.get(url)
    print("back to homepage")
    time.sleep(2)

#step6
    games = driver.find_element(By.XPATH, "//a[@id='mvl-flyout-button-5']")
    actions.move_to_element(games).perform()
    time.sleep(2)
    all_games = driver.find_element(By.XPATH, "//a[normalize-space()='See all Games']")
    actions.move_to_element(all_games).perform()
    actions.click(all_games).perform()
    time.sleep(2)

#step7
    video_games = driver.find_elements(By.XPATH, "//div[@class='LOBCard__Image_Wrapper']")
    print("Total games: ", len(video_games))
    for i in range(5):
        print(f"Opening game {i + 1}")
        video_games[i].click()
        time.sleep(2)

        print("Game page opened")
        driver.back()
        time.sleep(2)

#step8
    driver.execute_script("window.scrollBy(0,1000);")
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,-1000);")
    time.sleep(3)
    driver.get(url)

#step9
    searchbox = driver.find_element(By.ID, "search")
    searchbox.click()
    time.sleep(2)
    search_box2 = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_box2.send_keys("deadpool")
    search_box2.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.quit()




except Exception as e:
    print(f"error occured: {e}")
finally:
    driver.quit()
    print("browser closed")