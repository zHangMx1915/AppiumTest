# coding=utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from file_tools.log import Log


# 通用方法
class Public:

    def __init__(self):
        self.log = Log()

    # 判断执行元素是否需要添加延时
    def wait_time(self, element):
        for i in element:                   # 判断元素执行是否有加延时时间值
            if i == 'time':
                t = int(element['time'])
                time.sleep(t)

    #  首次启动系统权限弹窗
    def permission(self , driver, file_name):
        va = ''
        for i in range(5):
            loc = ("xpath", "//*[@text='允许']")
            locs = ("xpath", "//*[@text='始终允许']")                    # 关闭权限弹窗的按钮字符
            try:
                try:
                    e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                    e.click()
                    logs = loc + '跳过权限窗口'
                    self.log.mylog(logs, va)
                except:
                    e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(locs))
                    e.click()
                    logs = locs + '跳过权限窗口'
                    self.log.mylog(logs, va)
            except:
                pass

    #  滑动屏幕页面
    def window_slip(self, driver, element, file_name, times=500):   # other=0.5,
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

    # 截图
    def cut_shot(self, driver, path):
        test_time = (time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
        screen_save_path = path + test_time + '.png'
        driver.get_screenshot_as_file(screen_save_path)

    # 计算坐标
    def coordinate(self, driver, element):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        print('当前设备屏幕尺寸' + '：' + str(x) + ' ' + str(y))
        x1 = x * float(element['x'])
        y1 = y * float(element['y'])
        return x1, y1

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

    # toast消息判断
    def find_toast(self, driver, element, timeout=10, poll_frequency=0.3):
        va= ''
        try:
            logs = element['name']
            self.log.mylog(logs, va)
            text = element['value']
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            t = WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            print(t.text)
        except:
            logs = '缺少toast消息'
            self.log.mylog(logs, va)
            print(logs)
