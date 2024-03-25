# import necessary classes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# create driver object 
#driver = webdriver_manager.Firefox()

# A URL that delays loading
driver.get("https://www.geeksforgeeks.org/explicit-waits-in-selenium-python/?ref=lbp")

try:
	# wait 10 seconds before looking for element
	element = WebDriverWait(driver, 5).until(
		EC.presence_of_element_located((By.ID, "myDynamicElement"))
	)
finally:
	# else quit
	driver.quit()
