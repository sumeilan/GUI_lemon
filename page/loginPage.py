# -*- coding:UTF-8 -*-
import time
from base import element_exist


class LoginPage(element_exist.Action):
    login_btn_loc = ("showLoginBtn")
    phone_input_loc = ("mobileEditText")
    send_sms_btn_loc = ("sendSmsBtn")
    code_input_loc = ("codeInputView")
    avatar_loc = ("homeAvatarView")

    def login_in(self):
        time.sleep(2)
        self.find_element(self.login_btn_loc).click()
        time.sleep(5)
        self.find_element(self.phone_input_loc).send_keys('12345678998')
        self.find_element(self.send_sms_btn_loc).click()
        time.sleep(3)
        self.find_element(self.code_input_loc).send_keys('8998')

    def login_out(self):
        self.find_element(self.avatar_loc).click()
        time.sleep(2)
