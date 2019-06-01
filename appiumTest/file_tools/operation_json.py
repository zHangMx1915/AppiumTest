# coding=utf-8
import json


# 读取json
def get_config(conf):
    with open("../test_file/appiumFile/config/data_config.json", 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    conf_data = data[conf]
    return conf_data
