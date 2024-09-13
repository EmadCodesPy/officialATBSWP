from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://stackoverflow.com/users/login?ssrc=head&returnurl=https\\%3a%2f%2fstackoverflow.com\\%2f')
emailElem = browser.find_element(By.ID, 'email')
emailElem.send_keys('emadcoding@gmail.com')
passElem = browser.find_element(By.ID, 'password')
passElem.send_keys('8Rd7VUdtEBFN3B')
passElem.submit()