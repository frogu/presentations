from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://google.com")
fld=driver.find_element_by_id('gbqfq')
fld.send_keys('Anonimowi Admini')

