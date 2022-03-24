# coding=UTF-8
# @Time: 2022/2/2 12:54
# @Author: 张 翔
# @File: testXwlt.py
# @Software: PyCharm
# @email: 1456978852@qq.com


import xlwt

# workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象
# worksheet = workbook.add_sheet("sheet1")    # 创建工作表
# worksheet.write(0, 0, "hello")              # 写入数据，第一行参数“行”，第二个参数“列”，第三个参数内容
# workbook.save("students.xls")               # 保存数据表

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("sheet1")
for i in range(1, 10):
	for j in range(1, i+1):
		worksheet.write(i-1, j-1, f"{j}*{i}={i*j}")
workbook.save("students.xls")