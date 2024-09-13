from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element(By.TAG_NAME, 'html')
print('Starting game')
gameOver = browser.find_element(By.CLASS_NAME, 'game-container')
while gameOver.text[0] != 'G':
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT) 
    gameOver = browser.find_element(By.CLASS_NAME, 'game-container')

score = browser.find_element(By.CLASS_NAME, 'score-container')
score = score.text
print('Game over!')
print(f'Your final score was {score}')