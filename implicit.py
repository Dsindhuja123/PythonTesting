# import webdriver 
from selenium import webdriver 

driver = webdriver.Firefox() 

# set implicit wait time 
driver.implicitly_wait(10) # seconds 

# get url 
driver.get("https://www.instagram.com/?hl=en") 

# get element after 10 seconds 
myDynamicElement = driver.find_element_by_id("myDynamicElement") 
