# coding=utf-8
import re

print(re.findall('a[1*-]b', 'a1b a*b a-b'))  # ['a1b', 'a*b', 'a-b']
print(re.findall('a[^1*-]b', 'a1b a*b a-b a=b'))  # ['a=b']
print(re.findall('a[0-9]b', 'a1b a*b a-b a=b'))  # ['a1b']
print(re.findall('a[a-z]b', 'a1b a*b a-b a=b aeb'))  # ['aeb']
print(re.findall('a[a-zA-Z]b', 'a1b a*b a-b a=b aeb aEb'))  # ['aeb', 'aEb']
# print(re.findall('a\\c','a\c'))#对于正则来说a\\c确实可以匹配到a\c,但是在python解释器读取a\\c时，
# 会发生转义，然后交给re去执行，所以抛出异常
print(re.findall(r'a\\c', 'a\c'))  # r代表告诉解释器使用rawstring，即原生字符串，
# 把我们正则内的所有符号都当普通字符处理，不要转义

print(re.findall('ab+', 'ababab123'))  # ['ab', 'ab', 'ab']
print(re.findall('(ab)+123', 'ababab123'))  # ['ab']
print(re.findall('href="(.*?)"', '<a href="http://www.baidu.com">点击</a>'))  # ['http://www.baidu.com']
print(re.findall('href="(?:.*?)"', '<a href="http://www.baidu.com">点击</a>'))  # 取消分组优先(?: 正则表达式)

print(re.search('e', 'alex make love').group())  # e,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以通过
# 调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
print(re.match('e', 'alex make love'))  # None,同search,不过在字符串开始处进行匹配,完全可以用search+^代替match
print(re.split('[ab]', 'abcd'))  # ['', '', 'cd']，先按'a'分割得到''和'bcd',再对''和'bcd'分别按'b'分割

print(re.findall('d(\d)|\d', 'abcd123'))
print(re.findall('\w\\\\1', 'abc\123'))
print(re.findall('a[1*-]b', 'a1b a*b a-b'))
print(re.findall('a[^1*-]b', 'a1b a*b a-b a=b'))
print(re.findall(r'a\\c', 'a\c'))

print(re.search('ab+', 'abcdefg2345aaaaabbccdd').group())  # ab
