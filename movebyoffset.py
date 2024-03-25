from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("file:///C:/Users/dsindhuja/Desktop/Python1/selectable.html")


three = driver.find_element(By.NAME,"three")

l = three.location
s = three.size

print(f'Coordinates : {l} ')
print(f'size : {s} ')


actions = ActionChains(driver)
actions.move_by_offset(200,200)

time.sleep(5)
actions.click().perform()