# import webdriver 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# create webdriver object 
driver = webdriver.Chrome() 


driver.get("https://demoqa.com/login")


login = driver.find_element(By.ID,"login")

username = driver.find_element(By.ID,"userName")
password = driver.find_element(By.ID,"password")

username.send_keys("sindhu")
password.send_keys("Sindhu@123")


login.click()

try:
    element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID,"searchBox")))
    element.send_keys('Learn JavaScript')
    time.sleep(10)
    
finally:
    driver.close()
    
    



