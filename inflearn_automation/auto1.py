# https://www.inflearn.com/course/lecture?courseSlug=%EC%97%85%EB%AC%B4%EC%9E%90%EB%8F%99%ED%99%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC-pyautogui-%ED%81%AC%EB%A1%A4%EB%A7%81%EA%B8%B0%EC%B4%88&unitId=27319

import pyautogui
import time
#print(pyautogui.position())

# pyautogui.moveTo(500,500,3)
# pyautogui.moveTo(500,0,3)
# pyautogui.moveRel(0,200,2)
# pyautogui.moveRel(200,0,2)

#current positon ('search button')
#print(pyautogui.position()) # 20,100

pyautogui.moveTo(20,100,2)
#pyautogui.click(clicks=2, interval=2)
pyautogui.click()
time.sleep(1)
pyautogui.typewrite('import')
time.sleep(1)
pyautogui.click()