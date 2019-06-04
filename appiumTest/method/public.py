# coding=utf-8
from selenium.webdriver.support import expected_conditions as er
from selenium.webdriver.support.ui import WebDriverWait
import time
from file_tools import log


# 判断执行元素是否需要添加延时
def wait_time(element):
    for i in element:  # 判断元素执行是否有加延时时间值
        if i == 'time':
            t = int(element['time'])
            time.sleep(t)


# 截图
def cut_shot(driver, path, photo_num=1, time_wait=0.3):
    """
    num: 截图张数
    time：截图间隔时间
    """
    for j in range(int(photo_num)):
        test_time = (time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
        screen_save_path = path + test_time + '.png'
        driver.get_screenshot_as_file(screen_save_path)
        time.sleep(time_wait)
        j += 1
    


# 计算坐标
def coordinate(driver, element):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print('当前设备屏幕尺寸' + '：' + str(x) + ' ' + str(y))
    value = element['xy'].split(",")
    x1 = x * float(value[0].strip())
    y1 = y * float(value[1].strip())
    print('-' * 100, x1, y1)
    return x1, y1


#  首次启动系统权限弹窗
def permission(driver):
    va = ''
    for i in range(5):
        loc = ("xpath", "//*[@text='允许']")
        locs = ("xpath", "//*[@text='始终允许']")                    # 关闭权限弹窗的按钮字符
        # noinspection PyBroadException
        try:
            # noinspection PyBroadException
            try:
                e = WebDriverWait(driver, 1, 0.5).until(er.presence_of_element_located(loc))
                e.click()
                logs = str(loc) + '跳过权限窗口'
                log.mylog(logs, va)
            except Exception:
                e = WebDriverWait(driver, 1, 0.5).until(er.presence_of_element_located(locs))
                e.click()
                logs = str(locs) + '跳过权限窗口'
                log.mylog(logs, va)
        except Exception:
            pass


#  滑动屏幕页面
def window_slip(driver, element, times=500):   # other=0.5,
    va = ''
    logs = element['name']
    log.mylog(logs, va)
    start = float(element['start'])
    end = float(element['end'])
    other = float(element['other'])               # 滑动的中心位置
    n = int(element['n'])                         # 滑动次数
    direction = element['direction']
    wait_time(element)
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
def element_text(driver, element):
    va = ''
    logs = element['name']
    log.mylog(logs, va)
    wait_time(element)
    text = element['value1']
    el = driver.find_element_by_id(element['value'])
    if el.text == text:
        logss = '显示正确,显示为：' + str(el.text)
        print(logss)
        log.mylog(logss, va)
    else:
        logsa = '显示不正确,显示为：' + str(el.text)
        print(logsa)
        log.mylog(logsa, va)


# toast消息判断
def find_toast(driver, element, timeout=10, poll_frequency=0.3):
    va = ''
    try:
        logs = element['name']
        log.mylog(logs, va)
        text = element['value']
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
        t = WebDriverWait(driver, timeout, poll_frequency).until(er.presence_of_element_located(toast_loc))
        print(t.text)
    except Exception as msg:
        logs = '缺少toast消息' + str(msg)
        log.mylog(logs, va)
        print(logs)
