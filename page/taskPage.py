# -*- coding:UTF-8 -*-
import time
from base import element_exist


class TaskPage(element_exist.Action):
    login_btn_loc = ("showLoginBtn")

    def enter_page(self):
        self.driver.tap([(900, 1400), ])
        time.sleep(2)
