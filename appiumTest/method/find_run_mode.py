# coding=utf-8
from core import start_case

class JudgeMode:

    def __init__(self):
        self.run_case = start_case.GoTest()

        # 执行测试
    def judge_type(self, element, driver, ip):
        if element['type'] == 'id':
            self.run_case.ids(driver, element)
        elif element['type'] == 'xpath':
            self.run_case.xpath_type(driver, element)
        elif element['type'] == 'adb':
            self.run_case.adbs(driver, element, ip)
        elif element['type'] == 'tap':
            self.run_case.tap_type(driver, element)
        elif element['type'] == 'tab':
            self.run_case.tab(element, ip)
        elif element['type'] == 'wait':
            self.run_case.wait_activity(driver, element)
        elif element['type'] == 'text':
            self.run_case.element_text(driver, element)
        elif element['type'] == 'slip':
            self.run_case.window_slip(driver, element)
        elif element['type'] == 'toast':
            self.run_case.find_toast(driver, element)
        elif element['type'] == 'yao':
            self.run_case.repeat(driver, element)
