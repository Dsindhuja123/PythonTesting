from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://www.google.com")


#get all cookies
mycookies = driver.get_cookies()
print(len(mycookies))
print(mycookies)


#adding cookies
cookie = {'name' : 'cookiename' , 'value' : 'cookievalue'}
driver.add_cookie(cookie)
mycookies = driver.get_cookies()
print(len(mycookies))
print(mycookies)

#deleting cookie
driver.delete_cookie('cookiename')
mycookies = driver.get_cookies()
print(len(mycookies))
print(mycookies)

