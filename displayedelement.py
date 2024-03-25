from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.google.com/")

search_box = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')

print(search_box.is_displayed())
print(search_box.is_enabled())
print(search_box.is_selected())






