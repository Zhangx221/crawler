# coding=UTF-8
# @Time: 2022/2/1 12:10
# @Author: 张 翔
# @File: testRe.py
# @Software: PyCharm
# @email: 1456978852@qq.com


# 正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
# 创建模式对象

# pat = re.compile("AA")  # 此处的AA，是正则表达式，用来去验证其他的字符串
# m = pat.search("CBA")  # search字符串被校验的内容  search方法，进行比对查找

# m = pat.search("ABCAA")
# print(m)  # <re.Match object; span=(3, 5), match='AA'>

# m = pat.search("ABCAADDCCAAA")
# print(m)  # <re.Match object; span=(3, 5), match='AA'>

# 没有模式对象
# m = re.search("asd", "Aasd")  # 前面的字符串是规则（模板），后面的字符串是被检验的对象  # <re.Match object; span=(1, 4), match='asd'>
# print(m)

# print(re.findall("a", "ASDaDFGAa"))  # 前面字符串是规则（正则表达式），后面字符串是被检验的字符串  # ['a', 'a']

# print(re.findall("[A-Z]", "ASDaDFGAa"))  # ['A', 'S', 'D', 'D', 'F', 'G', 'A']

# print(re.findall("[A-Z]+", "ASDaDFGAa"))


# sub
print(re.sub("a", "A", "abcdcasd"))  # 找到a用A替换, 在第三个字符串中查找

# 建议在正则表达式中，被比较的字符前面加上r，避免转义字符的问题

