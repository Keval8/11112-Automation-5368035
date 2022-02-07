#  Create a PyTest program where you assert whether Youtube.com is displaying
#  at least 5 search results or not when you search for anything
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


def result_youtube():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/")

    Actions = ActionChains(driver)

    searchBar = driver.find_element(By.XPATH, "//*[@id='search']")
    searchBar.send_keys("Music")
    time.sleep(5)

    searchBar.send_keys(Keys.ENTER)

    time.sleep(5)

    result_count1 = driver.find_element(By.CLASS_NAME, "style-scope ytd-video-renderer")
    total_counts = result_count1.count()
    # print(total_counts)
    time.sleep(30)
    driver.close()
    driver.quit()
    # return total_counts
