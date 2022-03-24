# coding=UTF-8
# @Time: 2022/1/30 1:36
# @Author: 张 翔
# @File: spider-souhu.py
# @Software: PyCharm
# @email: 1456978852@qq.com


from bs4 import BeautifulSoup      # 网页解析，获取数据
import urllib.request,urllib.error  # 指定URL,获取网页数据
import pandas as pd


def main():
	baseurl = "https://tv.sohu.com/hotmovie/"
	# 1.爬取网页
	datalist = getData(baseurl)
	savepath = ".\\souhuTop.xls"
	# 3.保存数据
	saveData(datalist, savepath)


# 1.爬取网页
def getData(baseurl):
	datalist = []
	for i in range(0, 1):    # 调用获取页面信息的函数，10次
		url = baseurl
		html = askURL(url)    # 保存获取到的网页源码

		# 2.逐一解析数据
		soup = BeautifulSoup(html, "html.parser")
		for item in soup.find_all("a", class_="at"):  # 查找符合要求的字符串，形成列表。
			# print(item.split())
			data = []  # 保存一部电影的所有信息
			item = str(item)
			title = item.split()[-1]
			if len(title.split('"')) > 2:
				title = title.split('"')[1]
			else:
				title = title

			data.append(title)

			herf = item.split()[3]
			herf = herf.split('"')[-2]
			data.append(herf)

			datalist.append(data)   # 把处理好的一部电影信息放入datalist
	return datalist


# 得到指定一个url的网页内容
def askURL(url):
	head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"
	}
	# 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
	request = urllib.request.Request(url, headers=head)
	html = ""
	try:
		response = urllib.request.urlopen(request)
		html = response.read().decode("utf-8")
	except urllib.error.URLError as e:
		if hasattr(e, "code"):  # hasattr(object, name) 函数,判断object是否包含name属性
			print(e.code)
		if hasattr(e, "reason"):
			print(e.reason)

	return html


# 3.保存数据
def saveData(datalist, savepath):
	datalist = pd.DataFrame(datalist, columns=["电影名", "链接"])
	datalist.to_excel(savepath)

if __name__ == '__main__':
	main()
	print("爬取完毕")
