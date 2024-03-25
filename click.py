from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("file:///C:/Users/dsindhuja/Desktop/Python1/selectable.html")
time.sleep(5)

one = driver.find_element(By.NAME,"one")
two = driver.find_element(By.NAME,"two")
three = driver.find_element(By.NAME,"three")

actions = ActionChains(driver)

actions.click(one)
actions.click(two)
actions.click(three)


actions.perform()