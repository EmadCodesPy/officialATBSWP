import pyautogui

for i in range(3): #This moves the position of the mouse
    pyautogui.moveTo(100,100, duration=0.25)
    pyautogui.moveTo(200,100, duration=0.25)
    pyautogui.moveTo(200,200, duration=0.25)
    pyautogui.moveTo(100,200, duration=0.25)

for i in range(3): #Moves mouse from relative position
    pyautogui.moveRel(500,0,duration=0.25)
    pyautogui.moveRel(-500,0,duration=0.25)

pyautogui.moveTo(1500,800,duration=0.5)
print(pyautogui.position()) #Returns current position of mouse