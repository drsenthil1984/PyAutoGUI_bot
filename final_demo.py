import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5


print("step 1:open the chrome browser...")
time.sleep(2)

pyautogui.hotkey('command', 'space', interval=0.1)
time.sleep(1)

pyautogui.write('chrome', interval=0.15)    
time.sleep(1)

pyautogui.press('enter')
time.sleep(3)

print("step 2:open the website...")
pyautogui.hotkey('command', 't', interval=0.1)
time.sleep(1)
pyautogui.write('https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671?type=locality&city=chennai', interval=0.15)
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)

print("step 3: copy the full data of the website...")
pyautogui.hotkey('command', 'a', interval=0.1)
time.sleep(1)
pyautogui.hotkey('command', 'c', interval=0.1)
time.sleep(1)       

print("step 4: open the text editor...")
pyautogui.hotkey('command', 'space')
time.sleep(1)

pyautogui.write('textedit', interval=0.15)
time.sleep(1)

pyautogui.press('enter')
time.sleep(3)

# Close the TextEdit file chooser
pyautogui.press('esc')
time.sleep(1)

# Create a new blank document
pyautogui.hotkey('command', 'n')
time.sleep(2)

print("step 5: paste the data in textedit..")
pyautogui.hotkey('command', 'v', interval=0.1)
time.sleep(2)

#pyautogui.hotkey('command', 's', interval=0.1)
#time.sleep(1)       


