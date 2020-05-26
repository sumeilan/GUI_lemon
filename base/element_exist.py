# def is_element_exist(self, element):
#     try:
#         if self.driver.find_element_by_id(element):
#             return True
#         else:
#             return False
#     except Exception as e:
#         print(e)


class Action(object):
    # 初始化
    def __init__(self, se_driver):
        self.driver = se_driver

    def is_element_exist(self, element):
        try:
            return self.driver.find_element_by_id(element)
        except Exception as e:
            print(e)

    # 重写元素定位的方法
    def find_element(self, loc):
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print("未找到%s" % (self, loc))