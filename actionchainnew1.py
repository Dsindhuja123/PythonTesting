from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/dsindhuja/Desktop/Python1/selectable.html")
time.sleep(10)

one = driver.find_element(By.NAME,"one")
two =  driver.find_element(By.NAME,"two")
three =  driver.find_element(By.NAME,"three")
four =  driver.find_element(By.NAME,"four")
five =  driver.find_element(By.NAME,"five")


actions = ActionChains(driver)
actions.key_down(keys.Keys.CONTROL)

actions.click(one)
actions.click(two)
actions.click(three)
actions.click(four)
actions.click(five)

actions.perform()