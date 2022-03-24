# coding=UTF-8
# @Time: 2022/1/31 10:36
# @Author: 张 翔
# @File: testBs4.py
# @Software: PyCharm
# @email: 1456978852@qq.com


"""
BeautifulSoup4将复杂HTML文档转化成一个复杂的树形结构，每个节点都是pythno对象，所有对象可以归纳为四种：

- Tag
- NavigableString
- BeautifulSoup
- Comment
"""
import re

from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")  # 使用解析器html.parser

# print(bs.title)  # <title>百度一下·你就知道</title>
# print(bs.a)
# print(bs.head)

# print(type(bs.head))  # <class 'bs4.element.Tag'>

# 1.Tag  标签及其内容：拿到它所找到的第一个内容


# print(bs.title.string)  # 百度一下·你就知道
# print(type(bs.title.string))  # <class 'bs4.element.NavigableString'>

# 2.NavigableString  标签里的内容（字符串）

# print(bs.a.attrs)  # {'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'}
# # 拿到一个标签里的所有属性

# print(type(bs))  # <class 'bs4.BeautifulSoup'>
# 3.BeautifulSoup 表示整个文档

# print(bs.name)  # [document]
# print(bs)

# print(bs.a.string)  # 新闻
# print(type(bs.a.string))  # <class 'bs4.element.Comment'>

# 4.Comment 是一个特殊的NavigableString，输出的内容不包含注释符号


# —————————————————————————————————————————————————————— #

# 1.文档的遍历

# print(bs.head.contents)
# print(bs.head.contents[1])

# 更多内容搜索文档

# 2.文档的搜索 （经常使用）

# (1)find_all()
# 	字符串过滤：会查找与字符串（a）完全匹配的内容
# t_list = bs.find_all("a")
# print(t_list)

# (2)bs.find_all()
# 正则表达式搜索：使用search()方法来匹配内容
# t_list = bs.find_all(re.compile("a"))
# print(t_list)


# 方法： 传入一个函数（方法），根据函数的要求来搜素
# def name_is_exists(tag):
# 	return tag.has_attr("name")  # 返回有name属性
#
# t_list = bs.find_all(name_is_exists)
# # print(t_list)
# for item in t_list:
# 	print(item)

# kwargs 参数
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)  # 显示有class的标签
# t_list = bs.find_all(href="http://news.baidu.com")
#
# for item in t_list:
# 	print(item)


# text参数
# t_list = bs.find_all(text="hao123")  # 查找拥有特定文本的内容
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
# t_list = bs.find_all(text=re.compile("\d"))  # 应用正则表达式查找包含数字的
#
# for item in t_list:
# 	print(item)


# limit参数
# t_list = bs.find_all("a", limit=3)  # 只搜索查找到的前3个
#
# for item in t_list:
# 	print(item)


# t_list = bs.select("title")  # 通过标签来查找 [<title>百度一下·你就知道</title>]
# t_list = bs.select(".mnav")  # 通过类名来查找
# t_list = bs.select("#u1")      # 通过id来查找
# t_list = bs.select("a[class='bri']")  # 通过属性值来查找
# t_list = bs.select("head > title")  # 通过子标签来查找  找到head里面的title
# for item in t_list:
# 	print(item)

t_list = bs.select(".mnav ~ .bri")
print(t_list[0].get_text())







