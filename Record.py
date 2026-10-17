import keyboard
import time

live = False
recordFile = "program.txt"
size = 0

prevTime = 0            

def record(key):
    global prevTime
    if key.event_type == keyboard.KEY_DOWN:
        currentTime = time.time()
        timeInterval = currentTime - prevTime
        with open(recordFile, "a") as file:
            file.write(key.name + "\n")
            file.write(str(timeInterval) + "\n")
            prevTime = currentTime

while True:
    if keyboard.is_pressed('f8') and live == False:
        time.sleep(0.5)
        with open(recordFile, "w") as file:
            pass
        prevTime = time.time()
        keyboard.hook(record)
        live = True
        time.sleep(1)
    elif keyboard.is_pressed('f8') and live == True:
        with open(recordFile, "a") as file:
            file.close()
        break

       