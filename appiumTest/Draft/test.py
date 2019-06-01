# coding=utf-8
import csv

# def read_csv(self,    file_name):
# path = '../test_file/appiumFile/case'
# # file_path = path + '/' + 'temp.csv'
# file_path = 'D:/python/testApi-master/test_file/appiumFile/case/temps.csv'
# with open(file_path) as csvfile:
#     reader = [each for each in csv.DictReader(csvfile)]     # 读取csv文件

# for i in reader:
# 	# print(type(i['mm']))
# 	# print(i['mm'])
# 	if i['mm']: 
# 		print(1)
# 	else:
# 		print(2)

with open('D:/python/testApi-master/test_file/appiumFile/log/2019-06-01 16-58-35.txt', 'r',  encoding='utf-8') as ms:
	array=ms.read()
	print(array)