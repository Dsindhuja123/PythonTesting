
'''
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
  
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
  
# create webdriver object
driver = webdriver.Firefox()
  
# create action chain object
action = ActionChains(driver)

   
menu = driver.find_element(By.CSS_SELECTOR,".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR,".nav # submenu1")
 
ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

menu = driver.find_element(By.CSS_SELECTOR,".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR,".nav # submenu1")
 
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()

'''

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
  
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
  
# create webdriver object
driver = webdriver.Firefox()
  
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
  
# get element 
element = driver.find_element(By.LINK_TEXT,"Courses")

element = driver.find_element(By.ID,"passwd-id") 
element = driver.find_element(By.NAME,"passwd") 
  
# create action chain object
action = ActionChains(driver)
action.context_click(on_element = element)
action.double_click(on_element = element)  
  
# click the item
action.click(on_element = element)
  
# perform the operation
action.perform()





