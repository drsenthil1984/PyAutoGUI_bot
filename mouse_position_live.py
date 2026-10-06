import pyautogui
import time

print("Move the mouse around. Press Ctrl+C in Terminal to stop.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"x={x}, y={y}", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped")