'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
# Initialize the webdriver
driver = webdriver.Chrome()
    # Open the HTML file
driver.get("file:///C:/Users/dsindhuja/Desktop/Selenium/index.html")
 
    # Create Operation
#new_task_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'new-task-input')))
#new_task_input.send_keys('New Task')
#add_task_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'add-task-button')))
#add_task_button.click()


task1 = driver.find_element(By.XPATH,'//*[@id="task1"]') 
#task1.send_keys('New Task')
task1.send_keys('New Task')

if "index.html" in driver.current_url:
    print("Success")
else:
    print("Failure")
driver.quit()
'''








from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
# Initialize the webdriver
driver = webdriver.Chrome()
 
try:
    # Open the HTML file
    driver.get("file:///C:/Users/dsindhuja/Desktop/Selenium/index.html")
 
    # Create Operation
    new_task_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'new-task-input')))
    new_task_input.send_keys('New Task')
    add_task_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'add-task-button')))
    add_task_button.click()
 
    # Read Operation
    todo_list = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'todo-list')))
    assert 'New Task' in todo_list.text
 
    # Update Operation
    task_to_update = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-task-button"]')))
    task_to_update.click()
    #task_to_update.clear()
    #task_to_update.send_keys('Updated Task')
    #task_to_update.send_keys(Keys.ENTER)
 
    # Verify the update
    time.sleep(10)  # Wait for the update to reflect
    updated_task = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-task-button"]')))
    assert updated_task.text == 'Updated Task'
 
    # Delete Operation
    task_to_delete = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="task1"]/button[2]')))
    task_to_delete.click()
    
    # Verify the deletion
    time.sleep(10)  # Wait for the deletion to reflect
    try:
        deleted_task = driver.find_element(By.XPATH, '//*[@id="task1"]/button[2]')
        assert False, "Deletion failed"
    except:
        pass  # Deletion successful
 
finally:
    # Close the browser
    if "index.html" in driver.current_url:
        print("Success")
    else:
        print("Failure")
        driver.quit()
    


