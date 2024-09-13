from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com') 

#recall Selenium’s WebDriver Methods for Finding Elements
#recall WebElement Attributes and Methods

try:
    elem = browser.find_element_by_class_name('col-sm-12')
    print('Found <%s> element with that class name!' %(elem.tag_name))
except:
    print('Was not able to find element with that class name.')
    