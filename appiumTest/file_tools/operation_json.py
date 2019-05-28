# coding=utf-8
import json


class OpenJson:

    # 读取json
    def operation_json(self):
        with open("../test_file/appiumFile/config/data_config.json", 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        return data

    # 根据关键字获取数据
    def get_config(self, conf):
        data = self.operation_json()
        conf_data = data[conf]
        return  conf_data
