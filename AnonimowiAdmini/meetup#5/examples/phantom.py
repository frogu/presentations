from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("http://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_id("search_button_homepage").click()
driver.get_screenshot_as_file('skrinszot.png')
driver.quit
