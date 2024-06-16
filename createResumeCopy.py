#! python3

import pyautogui, time

#pyautogui.locateCenterOnScreen('c:\\users\\wanth\\mypythonscripts\\pyautogui\\screenshot_copy_resume.png')
pyautogui.moveTo((652, 713),duration= 0.5)
pyautogui.doubleClick((652, 713))

# pause
time.sleep(4)

# make a copy
pyautogui.moveTo((110, 190), duration= 0.5)
pyautogui.click((110, 190))
pyautogui.moveTo((160, 340), duration= 0.5)
pyautogui.click((160, 340))

# type doc name
pyautogui.typewrite('Anthony Tong Resume- ', interval=0.1)
# press enter
pyautogui.typewrite(['enter'])

#print("Copy created")

