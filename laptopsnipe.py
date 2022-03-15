from datetime import datetime
import time
from pynput.keyboard import Key, Controller
import pyautogui
keyboard = Controller()
def type_send(msg):
    keyboard.type(str(msg))
    keyboard.press(Key.enter)
def timenow():
    now = datetime.now()
    return(now.strftime("%H:%M:%S"))
print("Current Time =", timenow())
timestart = input("when to send message in hh:mm:ss = ")
numbertobuy = input("number of laptops to buy = ")
while True:
    if timenow() >= timestart:
        type_send("pls buy laptop " + numbertobuy)
        time.sleep(0.2)
        pyautogui.click()
        while True:
            time.sleep(3600)
            type_send("pls buy laptop " + numbertobuy)
            time.sleep(0.2)
            pyautogui.click()
