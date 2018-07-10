#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rpy2.robjects as robjects
# 此时，有三种方法调用R对象
# 第一种
print(robjects.r['pi'])
# 第二种
print(robjects.r('pi'))
# 这种方法从某种程度上讲是万能的，因为可以将任意大小和长度的R代码写成一个python字符串，之后通过robjects.r('Rcode')调用执行
# 第三种
print(robjects.r.pi)
# 这种方法对于名称中有“点号”的变量会出问题，比如data.frame/read.csv等，所以推荐使用第一种方法

