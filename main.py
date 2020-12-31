import pyautogui as p
import time
import random

while 1:
    for x in range(1, 11):
        for x in range(1, 4):
            p.hotkey('ctrl', 'v')
            p.write(",")
            p.write('\n')
            time.sleep(5)
        p.hotkey('ctrl', 'v')
        p.write("sell coql")
        p.write('\n')
        time.sleep(1)
        p.hotkey('ctrl', 'v')
        p.write("sell iron")
        p.write('\n')
        time.sleep(1)
        p.hotkey('ctrl', 'v')
        p.write("sell gold")
        p.write('\n')
        time.sleep(1)
    p.hotkey('ctrl', 'v')
    p.write("repqir")
    p.write('\n')
    time.sleep(1)