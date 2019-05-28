# coding=utf-8
import time
import os
from method.public import Public
from file_tools.log import Log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 执行元素
class GoTest:

    def __init__(self):
        self.log = Log()
        self.public = Public()

    # 判断执行元素是否需要添加延时
    def wait_time(self, element):
        for i in element:                                     # 判断元素执行是否有加延时时间值
            if i == 'time':
                t = int(element['time'])
                time.sleep(t)

    # id 和id_send_keys
    def ids(self, driver, element):  # 未完成
        logs = element['name']
        value = element['value']
        value1 = element['value1']
        print(logs, value, value1)
        self.wait_time(element)
        if not value1:
            driver.find_element_by_id(value).click()
            va = 'driver.find_element_by_id(%s)' % value
        else:
            driver.find_element_by_id(value).send_keys(value1)
            va = 'driver.find_element_by_id(%s).send_keys(%s)' % (value, value1)
        self.log.mylog(logs, va)

    # xpath方法
    def xpath_type(self, driver, element):
        logs = element['name']
        value = element['value']
        value1 = element['value1']
        va = 'driver.find_element_by_xpath(%s).click(%s)' % (value, value1)
        self.log.mylog(logs, va)
        self.wait_time(element)                          # 判断执行元素是否需要添加延时
        driver.find_element_by_xpath(value).click()

    # tap方法
    def tap_type(self, driver, element):
        logs = element['name']
        value = element['value']
        va = 'driver.tap(%s)' % value
        self.log.mylog(logs, va)
        self.wait_time(element)                          # 判断执行元素是否需要添加延时
        driver.tap(value)

    # adb方法
    def adbs(self, driver, element, ip):
        logs = element['name']
        value = element['value']
        value1 = element['value1']
        # x = element['x']
        # y = element['y']
        self.wait_time(element)                          # 判断执行元素是否需要添加延时
        if not value1:
            va = 'os.system(%s)' % value
            self.log.mylog(logs, va)
            os.system("adb -s %s shell input text '%s'" % (ip, value))
        else:
            print('sen_keys')
            xs, ys = self.public.coordinate(driver, element)
            va = ('adb -s %s shell input tap' % ip + ' ' + str(xs) + ' ' + str(ys))
            self.log.mylog(logs, va)
            os.system(va)

    # tab键方法，光标进入下一个输入框
    def tab(self, element, ip):
        logs = element['name']
        value = element['value']
        va = 'adb -s %s shell input keyevent %s' % (ip, value)
        self.log.mylog(logs, va)
        self.wait_time(element)                          # 判断执行元素是否需要添加延时
        os.system(va)

    # 等待指定页面出现
    def wait_activity(self, driver, element):
        logs = element['name']
        value = element['value']
        va = "driver.wait_activity(%s, 30)" % value
        self.log.mylog(logs, va)
        self.wait_time(element)
        driver.wait_activity(value, 30)

    # toast消息判断
    def find_toast(self, driver, element, timeout=10, poll_frequency=0.3):
        va = ''
        try:
            logs = element['name']
            text = element['value']
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            t = WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            self.log.mylog(logs, va)
            print(t.text)
        except:
            logs = '缺少toast消息'
            self.log.mylog(logs, va)
            print(logs)

    def window_slip(self, driver, element, times=500):   # other=0.5,
        va = ''
        logs = element['name']
        self.log.mylog(logs, va)
        start = float(element['start'])
        end = float(element['end'])
        other = float(element['other'])               # 滑动的中心位置
        n = int(element['n'])                         # 滑动次数
        direction = element['direction']
        self.wait_time(element)
        t = times                                # 滑动时间
        size = driver.get_window_size()          # 获取屏幕大小，size = {u'width': 720, u'height': 1280}
        if direction == 'vertical':              # 上下滑动
            x1 = size['width'] * other
            y1 = size['height'] * start
            y2 = size['height'] * end
            for i in range(n):
                driver.swipe(x1, y1, x1, y2, t)
        elif direction == 'horizontal':          # 左右滑动
            x1 = size['width'] * start
            x2 = size['width'] * end
            y1 = size['height'] * other
            for i in range(n):
                driver.swipe(x1, y1, x2, y1, t)

    # 获取元素的text文本值
    def element_text(self, driver, element):
        va = ''
        logs = element['name']
        self.log.mylog(logs, va)
        self.wait_time(element)
        text = element['value1']
        el = driver.find_element_by_id(element['value'])
        if el.text == text:
            logss = '显示正确,显示为：' + el.text
            print(logss)
            self.log.mylog(logss, va)
        else:
            logsa = '显示不正确,显示为：' + el.text
            print(logsa)
            self.log.mylog(logsa, va)

    # 多个重复id的元素操作,,协拍邀请演员出演角色招募，同意演员申请
    def repeat(self, driver, element):
        logs = element['name']
        value = element['value']
        value1 = element['value1']
        x = element['x']
        for i in range(4):
            va = 'driver.find_elements_by_id(%s)[%s].click(), ' \
                 'driver.find_element_by_id(%s)[%s].click()' % (value, i, value1, i)
            self.log.mylog(logs, va)
            time.sleep(1)
            try:
                try:
                    driver.find_elements_by_id(value)[i].click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[@text='%s']" % x).click()
                    break
                except:
                    self.window_slip(driver, element)
                    time.sleep(1)
                    driver.find_element_by_id(value1).click()
                    break
            except:
                driver.back()
