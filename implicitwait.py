from selenium import webdriver 
from selenium.webdriver.common.by import By

# create webdriver object 
driver = webdriver.Chrome()

driver.implicitly_wait(20)

driver.get("https://demoqa.com/login")

username = driver.find_element(By.ID,"userName")
password = driver.find_element(By.ID,"password")

login = driver.find_element(By.ID,"login")

username.send_keys("sindhu")
password.send_keys("Sindhu@123")


login.click()
	


