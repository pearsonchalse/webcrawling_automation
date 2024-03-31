import pyautogui

print(pyautogui.position())

# pyautogui.move(20,100)
# pyautogui.click(20,100)

# i = pyautogui.locateOnScreen('8.png')
# print(i)
# q = pyautogui.center(i)
# pyautogui.click(q)

i = pyautogui.locateCenterOnScreen('8.png')
pyautogui.click(i)