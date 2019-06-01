# coding=utf-8
import csv
# import yaml
# from selenium.common.exceptions import NoSuchElementException   # 异常处理


# 读取csv文件元素
def read_csv(file_name):
    path = '../test_file/appiumFile/case'
    file_path = path + '/' + file_name
    with open(file_path) as csvfile:
        reader = [each for each in csv.DictReader(csvfile)]     # 读取csv文件
    return reader


"""
file_path = "E:/testApi-master/test_file/appiumFile/login.csv"

a = ReadFile
m = a.read_csv('11')
for i in m:
    # print(type(i))
    mx = i['type']
    print(i)

    遍历元素，创建log文件，记录报错报错信息
    def run_test(self, list, driver, test):
        element = list[0]
        path = list[1]
        ip = list[2]
        ma = Public()
        mx = Log()
        file_name = mx.logfile(path, test)
        k = element + '/' + test
        with open(k) as csvfile:
            reader = [each for each in csv.DictReader(csvfile)]  # 读取csv文件
            for i in reader:
                time.sleep(1.5)
                try:
                    ma.judge_type(i, driver, file_name, ip)
                except NoSuchElementException as msg:
                    print(msg)
                    for i in range(5):
                        ma.cut_shot(driver, path)  # 出错时调用截图
                        time.sleep(0.5)
                        i += 1
                    time.sleep(10)
                    ma.judge_type(i, driver, file_name, ip)
                except ValueError:
                    time.sleep(5)
                    ma.judge_type(i, driver, file_name, ip)

    nons = ['姓名', '年龄', '身高', '电话']                           # 创建csv文件
    csvFile2 = open('E:/Action用例/loginin.csv', 'w', newline='')
    writer2 = csv.writer(csvFile2)
    writer2.writerow(nons)

    # 读取文件里的元素
    def find_element(self, driver, file_name, na):
        ma = Public()
        Modulelog = na['newRepertoire']['dec']                       # 测试模块名称
        print(Modulelog)
        for i in na["newRepertoire"]['locators']:
            time.sleep(0.3)
            ma.judge_type(i, driver, file_name, Modulelog)

    # 读取yaml文件
    def parseyaml(self, file_name, pageElement):                       # 传入yaml文件的路径，yaml文件夹名称
        pageElements = {}
        for fpath, dirname, fnames in os.walk(pageElement):      # 遍历读取yaml文件
            for name in fnames:
                if name == file_name:                            # 找到指定文件
                    yaml_file_path = os.path.join(fpath, name)   # yaml文件绝对路径
                    if ".yaml" in str(yaml_file_path):           # 排除一些非.yaml的文件
                        with open(yaml_file_path, 'r', encoding='utf-8') as f:
                            page = yaml.load(f)
                            pageElements.update(page)
        return pageElements
"""
