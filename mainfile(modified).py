from email.errors import FirstHeaderLineIsContinuationDefect
from hmac import digest
import select
import sys
import time
import random
import cooldowns as cd
import pynput
from pynput.keyboard import Key, Controller
import config
import pyautogui
keyboard = Controller()
def type_send(msg):
    keyboard.type(str(msg))
    time.sleep(2)
    keyboard.press(Key.enter)

def print_beg(scheduler):
    type_send("pls beg")
    scheduler.run_after(print_beg, cd.beg_cooldown)

def print_hunt(scheduler):
    type_send("pls hunt")
    scheduler.run_after(print_hunt, cd.hunt_cooldown)

def print_dig(scheduler):
    type_send("pls dig")
    scheduler.run_after(print_dig, cd.dig_cooldown)

def print_fish(scheduler):
    type_send("pls fish")
    scheduler.run_after(print_fish, cd.fish_cooldown)

def print_pm(scheduler):
    type_send("pls pm")
    time.sleep(random.randint(cd.pmAnswer_cooldown, cd.pmAnswer_cooldown+5))
    pyautogui.click()
    scheduler.run_after(print_pm, cd.pm_cooldown)

def print_hl(scheduler):
    type_send("pls hl")
    time.sleep(random.randint(cd.hlAnswer_cooldown, cd.hlAnswer_cooldown+5))
    pyautogui.click()
    scheduler.run_after(print_hl, cd.hl_cooldown)

def print_dep(scheduler):
    type_send("pls dep all")
    scheduler.run_after(print_dep, cd.dep_cooldown)

def print_scout(scheduler):
    type_send("pls scout")
    time.sleep(random.randint(1,6))
    pyautogui.click()
    scheduler.run_after(print_scout, 30)
class Scheduler:
    def __init__(self):
        self.ready = []
        self.waiting = []

    def run_soon(self, task):
        self.waiting.append((task, 0))

    def run_after(self, task, delay):
        self.waiting.append((task, time.time() + delay))

    def run_until_complete(self):
        while self.ready or self.waiting:
            while self.ready:
                self.ready.pop()(self)
                time.sleep(random.randint(3,7))
            for i in range(len(self.waiting) - 1, -1, -1):
                task, start_after = self.waiting[i]
                if start_after < time.time():
                    self.ready.append(task)
                    del self.waiting[i]

s = Scheduler()
time.sleep(5) #activate your window where you need to type within 5 sec
if config.beg:
    s.run_soon(print_beg)
if config.hunt:
    s.run_soon(print_hunt)
if config.fish:
    s.run_soon(print_fish)
if config.pm:
    s.run_soon(print_pm)
if config.hl:
    s.run_soon(print_hl)
if config.dig:
    s.run_soon(print_dig)
if config.scout:
    s.run_soon(print_scout)
if config.dep:
    s.run_soon(print_dep)
s.run_until_complete()

#use async in future
