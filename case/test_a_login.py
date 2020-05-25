# -*- coding:utf-8 -*-
import unittest
from ddt import ddt, data, unpack,file_data
from base import base_desired_caps
from page import loginPage

# 登录测试流程
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        base_desired_caps.base_desired_caps(self)

    def test_login(self):
        loginPage.login(self)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
