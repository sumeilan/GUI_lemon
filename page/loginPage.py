# -*- coding:UTF-8 -*-
import time
from base import element_exist


def login(self):
    time.sleep(15)
    exist = False
    self.driver.tap([(92, 98)])
    if self.driver.find_element_by_android_uiautomator('new UiSelector().text("欢迎登陆柠檬精")'):
        print("未登陆")
    else:
        print("已登录")
    time.sleep(5)

