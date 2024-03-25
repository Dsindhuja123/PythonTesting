from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/dsindhuja/Desktop/Python1/sortable.html")
time.sleep(5)


one = driver.find_element(By.NAME,"one")
four = driver.find_element(By.NAME,"four")

actions = ActionChains(driver)

actions.click_and_hold(one)
actions.release(four)

actions.perform()