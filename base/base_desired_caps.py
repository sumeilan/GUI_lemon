# -*- coding:utf-8 -*-
from appium import webdriver

import urllib3,logging
urllib3.disable_warnings()
#同时可以通过以下方式抓取日志
logging.captureWarnings(True)

# 在appium server 与手机端建立会话关系时，手机端需要告诉服务端设备相关的一些参数，根据这些参数服务端可以做出相应的处理。
def base_desired_caps(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '850ABM7AJMY2'
    desired_caps['appPackage'] = 'com.mallestudio.flash.debug'
    desired_caps['appActivity'] = 'com.mallestudio.flash.ui.splash.LauncherActivity'
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'
    desired_caps['noReset'] = 'True'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)