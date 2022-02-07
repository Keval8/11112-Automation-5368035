# Create a PyTest program where you assert whether Google.com is
# displaying at least 10 search results or not when you search for something.
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

def result_google():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://www.google.com/")

    Actions = ActionChains(driver)

    searchBar = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

    searchBar.send_keys("Movie")
    time.sleep(5)

    searchBar.send_keys(Keys.ENTER)

    time.sleep(5)

    result_count1 = driver.find_element(By.CLASS_NAME,"iUh30 qLRx3b tjvcx")
    total_counts = result_count1.count()
    # print(total_counts)
    time.sleep(30)
    driver.close()
    driver.quit()
    return total_counts
