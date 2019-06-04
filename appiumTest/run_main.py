# coding=utf-8
from file_tools import operation_csv
from core import start_up
from method import find_run_mode
from file_tools import operation_json
from file_tools import log
import time
from method import public, send_mail
# from selenium.common.exceptions import NoSuchElementException   # 异常处理
# import threading


# 获取app包名及设备ip
def get_config(conf):
    conf_data = operation_json.get_config(conf)
    ip = conf_data['deviceName']
    return conf_data, ip


def error_attempt(i, driver, ip):
    for j in range(5):
        time.sleep(3)
        # noinspection PyBroadException
        try:
            log_text = '等待3秒，第%s次尝试！' % (j + 1)
            log.mylog(log_text)
            print(log_text)
            find_run_mode.judge_type(i, driver, ip)
            return True
        except Exception:
            log_text = '第%s次尝试失败！' % (j + 1)
            log.mylog(log_text)
            print(log_text)


def go_test(case, driver, ip, path):
    case_data = operation_csv.read_csv(case)
    for i in case_data:
        time.sleep(1)
        if i['run'] == 'y':
            try:
                find_run_mode.judge_type(i, driver, ip)
            except Exception as msg:
                public.cut_shot(driver, path, 5)            # 截图
                print(msg)
                log.mylog('Error : ' + i['name'], str(msg))
                num = error_attempt(i, driver, ip)
                if num is None:
                    return None
    return True


class RunTest:

    def __init__(self):
        self.send_email = send_mail.SendEmail()

    def run_main_bak(self, conf, case_list):
        path = '../test_file/appiumFile/log'
        log.logfile()                              # 创建log文件
        conf_data, ip = get_config(conf)
        driver = start_up.login_app(conf_data)
        for case in case_list:
            case_data = operation_csv.read_csv(case)
            try:
                for i in case_data:
                    time.sleep(1)
                    if i['run'] == 'y':
                        try:
                            find_run_mode.judge_type(i, driver, ip)
                        except Exception as msg:
                            print(msg)
                            log.mylog('Error : ' + i['name'], str(msg))
                            for j in range(5):
                                public.cut_shot(driver, path)  # 出错时调用截图
                                time.sleep(0.5)
                                j += 1
                            try:
                                time.sleep(10)
                                find_run_mode.judge_type(i, driver, ip)
                            except Exception as msg:
                                log.mylog('Error : ' + i['name'], str(msg))
                                print(msg)
                                break
            except Exception as msg:
                log.mylog('Error : ' + str(msg))
                print(msg)
                break
        self.send_email.send_email(log.log_all())

    def run_main(self, conf, case_list):
        path = '../test_file/appiumFile/log'
        log.logfile()                              # 创建log文件
        conf_data, ip = get_config(conf)
        driver = start_up.login_app(conf_data)
        for case in case_list:
            num = go_test(case, driver, ip, path)
            if num is None:
                break
        self.send_email.send_email(log.log_all())


config = 'action'     # app和设备参数（在data_config.json)
# conf = 'action1'     # app和设备参数（在data_config.json)
case_list_m = ['login.csv', '发布招募.csv']
# '新建剧目.csv',

if __name__ == "__main__":
    run = RunTest()
    run.run_main(config, case_list_m)
