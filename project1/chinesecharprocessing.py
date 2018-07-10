#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mafan import encoding
from mafan import text
from mafan import simplify, tradify
from mafan import split_text
import mafan
from mafan import pinyin

# 对包含其他编码的文本转化成utf8格式
# filename = 'test.txt'  # name or path of file as string
# encoding.convert(filename)  # creates a file with name 'ugly_big5_utf-8.txt' in glorious utf-8 encoding

# 简体和繁体转化
print('-'*50)
string = u'这是麻烦啦'
print(tradify(string))  # convert string to traditional
print(simplify(tradify(string)))  # convert back to simplified

# 是否包含符号或者拉丁字符
print('-'*50)
flag = text.has_punctuation(u'这是麻烦啦')
print(flag)
flag = text.has_punctuation(u'这是麻烦啦.')
print(flag)
flag = text.has_punctuation(u'这是麻烦啦。')
print(flag)
flag = text.contains_latin(u'这是麻烦啦。')
print(flag)
flag = text.contains_latin(u'You are麻烦啦。')
print(flag)

# 判断是否是简体还是繁体
print('-'*50)
flag = text.is_simplified(u'这是麻烦啦')
print(flag)
flag = text.is_traditional(u'Hello,這是麻煩啦')  # ignores non-chinese characters
print(flag)

# 判断简体和繁体
print('-'*50)
flag = text.identify(u'这是麻烦啦') is mafan.SIMPLIFIED
print(flag)
flag = text.identify(u'這是麻煩啦') is mafan.TRADITIONAL
print(flag)
flag = text.identify(u'这是麻烦啦! 這是麻煩啦') is mafan.BOTH
print(flag)
flag = text.identify(u'This is so mafan.') is mafan.NEITHER  # or None
print(flag)

# 中文分词
print('-'*50)
bytelist = split_text(u"這是麻煩啦")
print(bytelist)
joinstr = ' '.join(split_text(u"這是麻煩啦"))
print(joinstr)

bytelist = split_text(u"這是麻煩啦", include_part_of_speech=True)
for k, v in bytelist:
    print(k, v)

# 中文拼音输出
pinyinstr = pinyin.decode("ni3hao3")
print(pinyinstr)

