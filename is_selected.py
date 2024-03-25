from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/checkboxes")

check_box1 = driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[1]')
check_box2 = driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[2]')

print(check_box1.is_selected())
print(check_box2.is_selected())