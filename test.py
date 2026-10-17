#keyboard.add_hotkey sehr cool
import pyautogui
import keyboard
import time

start = time.time()
time.sleep(1)
print("hello")
end = time.time()
print(end - start)


'''
live = False

def record(key):
    if key.event_type == keyboard.KEY_DOWN:
        with open("program.txt", "a") as file:
            file.write(key.name)
            file.write("\n")

while True:
    if keyboard.is_pressed('*') and live == False:
        keyboard.hook(record)
        live = True
        time.sleep(1)
    elif keyboard.is_pressed('*') and live == True:
        with open("program.txt", "a") as file:
            file.close()
        break
'''
       