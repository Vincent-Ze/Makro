import pyautogui
import time
import keyboard

pyautogui.FAILSAFE = True

recordFile = "program.txt"
live = False
char = 0
lineNum = 0

while True:
    if keyboard.is_pressed('f8'):
        with open(recordFile, "r") as file:
            for line in file:
                lineNum += 1
                char = line.strip()
                if (char != "f8"):
                    if (lineNum % 2 == 0):
                        timeNum = float(char)
                        time.sleep(timeNum)
                        print(char)
                    else:
                        print(char)
                        pyautogui.keyDown(char)
                        time.sleep(0.05)
                        pyautogui.keyUp(char)
                else:
                    break
                break        