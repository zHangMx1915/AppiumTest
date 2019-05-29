# coding=utf-8
from file_tools.operation_csv import ReadFile
from core.start_up import StartApp
from method.find_run_mode import JudgeMode
from file_tools.operation_json import OpenJson
from file_tools.log import Log
import time
from method import public
from selenium.common.exceptions import NoSuchElementException   # 异常处理


class RunTest:

    def __init__(self):
        self.read_file = ReadFile()
        self.start_app = StartApp()
        self.judge_mode = JudgeMode()
        self.get_conf = OpenJson()
        self.log = Log()
        self.public = public.Public()

    # 获取app包名及设备ip
    def get_config(self, conf):
        conf_data = self.get_conf.get_config(conf)
        ip = conf_data['deviceName']
        return conf_data, ip

    def go_start(self, conf, case_list):
        path = '../test_file/appiumFile/log'
        self.log.logfile()                              # 创建log文件
        conf_data, ip = self.get_config(conf)
        driver = self.start_app.login_app(conf_data)
        for case in case_list:
            case_data = self.read_file.read_csv(case)
            try:
                for i in case_data:
                    time.sleep(0.8)
                    if i['run'] == 'y':
                        try:
                            self.judge_mode.judge_type(i, driver, ip)
                        except Exception as msg:
                            print(msg)
                            self.log.mylog('Error : ' + i['name'], str(msg))
                            for i in range(5):
                                self.public.cut_shot(driver, path)  # 出错时调用截图
                                time.sleep(0.5)
                                i += 1
                            try:
                                time.sleep(10)
                                self.judge_mode.judge_type(i, driver, ip)
                            except Exception as es:
                                self.log.mylog('Error : ' + i['name'], str(es))
                                print(es)
                                break
            except Exception as e:
                self.log.mylog('Error : ' + str(e))
                print(e)
                break


conf = 'action'     # app和设备参数（在data_config.json)
# 用例
case_list = ['login.csv', '新建剧目.csv']

if  __name__== "__main__":
    run = RunTest()
    run.go_start(conf, case_list)
