# coding=UTF-8
# @Time: 2022/1/30 15:19
# @Author: 张 翔
# @File: testUrllib.py
# @Software: PyCharm
# @email: 1456978852@qq.com


import urllib.request


# # 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))  # 对获取到的网页源码进行utf-8的解码


# # 获取post请求
# import urllib.parse  # 解析器
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")  # 发出请求
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)  # post要传入data参数，get就不用了
# print(response.read().decode("utf-8"))


# 超时处理
# try:
# 	response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)  # 超时没响应会报错，正常是3~5秒
# 	print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:  # 如果有好几种错误在except后面用逗号分隔
# 	print("time out!")


# response = urllib.request.urlopen("http://www.baidu.com")
# # print(response.status)
# # print(response.getheaders())  # 获取所有头部信息
# print(response.getheader("Server"))  # 获取一个头部信息


import urllib.parse
# url = "http://httpbin.org/post"
# headers = {
# 	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"
# }
# data = bytes(urllib.parse.urlencode({"name":"eric"}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


url = "https://douban.com"
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))








