from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element(By.LINK_TEXT, 'YouTube')
linkElem.click()
browser.quit()
