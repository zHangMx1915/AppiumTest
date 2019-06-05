# coding=utf-8
from selenium.webdriver.support import expected_conditions as er
from selenium.webdriver.support.ui import WebDriverWait
import time
from file_tools import log


# 判断执行元素是否需要添加延时
# 判断执行元素是否需要添加延时
def wait_time(element):
    t = element['time']
    if t:
        time.sleep(int(t))


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
    logs = element['name']
    log.mylog(logs)
    wait_time(element)
    text = element['value1']
    el = driver.find_element_by_id(element['value'])
    if el.text == text:
        log_text = '显示正确,显示为：' + str(el.text)
        print(log_text)
        log.mylog(log_text)
    else:
        log_text = '显示不正确,显示为：' + str(el.text)
        print(log_text)
        log.mylog(log_text)
