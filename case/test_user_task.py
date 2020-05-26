# -*- coding:utf-8 -*-
import unittest
from ddt import ddt, data, unpack,file_data
from base import base_desired_caps
from page import taskPage

# 登录测试流程
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        base_desired_caps.base_desired_caps(self)

    def test_user_task(self):
        tp = taskPage.TaskPage(self.driver)
        tp.enter_page()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
