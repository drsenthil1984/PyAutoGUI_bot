import pyautogui
import time 
import pyscreeze

'''
pyautogui.typewrite('Hello, World!', interval=0.1)  # Type 'Hello, World!' with a 0.1 second delay between each character

#hot keys   
pyautogui.hotkey('cmd', 'c')  # Press cmd+C to copy
pyautogui.hotkey('cmd', 'v')  # Press cmd+v to paste
pyautogui.hotkey('cmd', 'a')  # Press cmd+A to select all
pyautogui.hotkey('cmd', 's')  # Press cmd+S to save

#pressing special keys 
pyautogui.press('enter')  # Press the Enter key
pyautogui.press('tab')  # Press the Tab key
pyautogui.press('backspace')  # Press the Backspace key
'''
#holding down keys
#pyautogui.keyDown('shift')  # Hold down the Shift key
#pyautogui.typewrite("this is upper case text")  # Type text while holding down Shift
#pyautogui.keyUp('shift')  # Release the Shift key

screenshot=pyautogui.screenshot('screenshot.png')  # Take a screenshot and save it as 'screenshot.png'
screenshot.save("final.png")  # save the screenshot
