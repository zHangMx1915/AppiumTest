# coding=utf-8
from core import start_case


# 执行测试
def judge_type(element, driver, ip):
    if element['type'] == 'id':
        start_case.ids(driver, element)
    elif element['type'] == 'xpath':
        start_case.xpath_type(driver, element)
    elif element['type'] == 'adb':
        start_case.adbs(driver, element, ip)
    elif element['type'] == 'tap':
        start_case.tap_type(driver, element)
    elif element['type'] == 'tab':
        start_case.tab(element, ip)
    elif element['type'] == 'wait':
        start_case.wait_activity(driver, element)
    elif element['type'] == 'text':
        start_case.element_text(driver, element)
    elif element['type'] == 'slip':
        start_case.window_slip(driver, element)
    elif element['type'] == 'toast':
        start_case.find_toast(driver, element)
    elif element['type'] == 'yao':
        start_case.repeat(driver, element)
