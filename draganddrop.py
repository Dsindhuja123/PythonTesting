from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/droppable")
time.sleep(5)

dragger = driver.find_element(By.ID,"draggable")
dropped = driver.find_element(By.ID,"droppable")


actions = ActionChains(driver)

'''actions.click_and_hold(dragger) #we can click and hold,release or else simply drag and drop method(we need to give the source,target location)
actions.release(dropped)'''

actions.drag_and_drop(dragger,dropped)

actions.perform()