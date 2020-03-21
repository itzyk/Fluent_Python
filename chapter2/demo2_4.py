# coding: utf-8
colors = ['black', 'white']
sizes = ['s', 'm', 'l']
tshirt = [(color, size) for color in colors for size in sizes]
print tshirt

tshirt = [(color, size) for size in sizes for color in colors]
print tshirt

symbols = '!@#$%^'
print tuple(ord(s) for s in symbols)

import array
a = array.array('I', (ord(s) for s in symbols))
print a

import os
_, filename = os.path.split('/Users/zhouyikai/MyWork/Fluent_Python')
print filename

# python3 拆包解包重要
# x, y, *other = range(5)
# 输出zyk            |   zzz   |   yyy
print '{:15}|{:^9}|{:^9}'.format('zyk', 'zzz', 'yyy')
# 输出  1.333  |   2.3457
print '{:^9.3f}|{:9.4f}'.format(1.333333, 2.3456789)  # ^站位中间，.3小数点保留3位

# 具名元祖
from collections import namedtuple
city = namedtuple('city', 'name country population coordinate')
tokyo = city('tokyo', 'jp', 36, (35, 139))

print tokyo.name
c = city._make(('china', 'nanjin', 12, (2, 3)))  # 接受一个可迭代对象生成这个类的实例
print c.name

'''
    切片
'''
s = 'bicycle'
print s[::3]   # bye
print s[::-1]  # elcycib
print s[::-2]  # eccb
l = list(range(20))
l[2:5] = [20, 30]    # [0, 1, 20, 30, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print l
del l[5:7]
print l   # [0, 1, 20, 30, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
l[2:5] = [100]  # l[2:5] = 100这个是错的，切片的赋值语句必须是可迭代的对象

# 列表组成的列表
board = [['_']*3]*3   # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 0     # [['_', '_', 0], ['_', '_', 0], ['_', '_', 0]] board包含了3个指向列表的引用
print board
board = [['_']*3 for i in range(3)]
board[1][2] = 0     # [['_', '_', '_'], ['_', '_', 0], ['_', '_', '_']]
print board

#
t = (1, 2, [11, 12])
t[2] += [13, 14]   # 不能对元祖的元素进行赋值操作 ，t会被修改也会有异常
print t



