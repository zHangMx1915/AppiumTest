# coding=utf-8
import time
import os
from method import public
from file_tools import log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as er


# 判断执行元素是否需要添加延时
def wait_time(element):
    t = element['time']
    if t:
        time.sleep(int(t))


def find_value(element):
    name, value, value1 = element['name'], element['value'], element['value1']
    return name, value, value1


# id 和id_send_keys
def ids(driver, element):
    name, value, value1 = find_value(element)
    print(name, value, value1)
    wait_time(element)
    if not value1:
        driver.find_element_by_id(value).click()
        va = 'driver.find_element_by_id(%s)' % value
    else:
        driver.find_element_by_id(value).send_keys(value1)
        va = 'driver.find_element_by_id(%s).send_keys(%s)' % (value, value1)
    log.mylog(name, va)


# xpath方法
def xpath_type(driver, element):
    name, value, value1 = find_value(element)
    va = 'driver.find_element_by_xpath(%s).click(%s)' % (value, value1)
    log.mylog(name, va)
    wait_time(element)                          # 判断执行元素是否需要添加延时
    driver.find_element_by_xpath(value).click()


# tap方法
def tap_type(driver, element):
    name, value, value1 = find_value(element)
    va = 'driver.tap(%s)' % value
    log.mylog(name, va)
    wait_time(element)                          # 判断执行元素是否需要添加延时
    driver.tap(value)


# adb方法
def adbs(driver, element, ip):
    name, value, value1 = find_value(element)
    wait_time(element)
    if value1:
        va = 'os.system(%s)' % value
        log.mylog(name, va)
        os.system("adb -s %s shell input text '%s'" % (ip, value))
    else:
        xs, ys = public.coordinate(driver, element)
        va = ('adb -s %s shell input tap' % ip + ' ' + str(xs) + ' ' + str(ys))
        log.mylog(name, va)
        os.system(va)


# tab键方法，光标进入下一个输入框
def tab(element, ip):
    name, value, value1 = find_value(element)
    va = 'adb -s %s shell input keyevent %s' % (ip, value)
    log.mylog(name, va)
    wait_time(element)                          # 判断执行元素是否需要添加延时
    os.system(va)


# 等待指定页面出现
def wait_activity(driver, element):
    name, value, value1 = find_value(element)
    va = "driver.wait_activity(%s, 13)" % value
    log.mylog(name, va)
    wait_time(element)
    print('等待指定页面出现' + va)
    driver.wait_activity(value, 30)


# toast消息判断
def find_toast(driver, element, timeout=10, poll_frequency=0.05):
    try:
        name, value, value1 = find_value(element)
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % value)
        t = WebDriverWait(driver, timeout, poll_frequency).until(er.presence_of_element_located(toast_loc))
        log.mylog(name, toast_loc)
        print(t.text)
    except Exception as e:
        logs = '未检测到toast消息' + str(e)
        log.mylog(logs)
        print(logs)


def window_slip(driver, element, times=1000):   # other=0.5,
    logs = element['name']
    log.mylog(logs)
    slip_conf = element['slide'].split(",")
    start = float(slip_conf[0].strip())
    end = float(slip_conf[1].strip())
    other = float(slip_conf[2].strip())            # 滑动的中心位置
    n = int(slip_conf[3].strip())
    direction = element['direction']
    wait_time(element)
    t = times                                # 滑动时间
    print(logs, start, end, other, n)
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
    logs = element['name']
    log.mylog(logs)
    wait_time(element)
    text = element['value1']
    el = driver.find_element_by_id(element['value'])
    if el.text == text:
        log_text = '显示正确,显示为：' + el.text
        print(log_text)
        log.mylog(log_text)
    else:
        log_text = '显示不正确,显示为：' + el.text
        print(log_text)
        log.mylog(log_text)


# 多个重复id的元素操作,,协拍邀请演员出演角色招募，同意演员申请
def repeat(driver, element):
    name, value, value1 = find_value(element)
    x = element['x']
    for i in range(4):
        va = 'driver.find_elements_by_id(%s)[%s].click(), ' \
             'driver.find_element_by_id(%s)[%s].click()' % (value, i, value1, i)
        log.mylog(name, va)
        time.sleep(1)
        # noinspection PyBroadException
        try:
            # noinspection PyBroadException
            try:
                driver.find_elements_by_id(value)[i].click()
                time.sleep(1)
                driver.find_element_by_xpath("//*[@text='%s']" % x).click()
                break
            except Exception:
                window_slip(driver, element)
                time.sleep(1)
                driver.find_element_by_id(value1).click()
                break
        except Exception:
            driver.back()
