import pyautogui

pyautogui.FAILSAFE = True #Will raise exception if mouse is moved to upper left corner
pyautogui.PAUSE = 1 #Waits 1 seconds before each function of the autogui

screenSize = pyautogui.size()
print(screenSize)
width, height = screenSize
print(width, height)