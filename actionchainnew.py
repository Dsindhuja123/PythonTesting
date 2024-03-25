from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

import webdriver_manager

driver = webdriver.Chrome()

driver.get("https://demoqa.com/selectable")
time.sleep(5)

one = driver.find_element(By.XPATH,'//*[@id="verticalListContainer"]/li[1]')
two = driver.find_element(By.XPATH,'//*[@id="verticalListContainer"]/li[2]')
three = driver.find_element(By.XPATH,'//*[@id="verticalListContainer"]/li[3]')
four = driver.find_element(By.XPATH,'//*[@id="verticalListContainer"]/li[4]')

actions = ActionChains(driver)

actions.click(one)
actions.click(two)
actions.click(three)
actions.click(four)

actions.perform()