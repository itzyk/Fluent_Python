# coding: utf-8

x = 'abc'
y = 'def'
dummy = [ord(x) for x in y]

# 输出结果为f，在python2中 列表推导会替换掉x的值，这在python3中，不会对x的值产生影响
print x

print dummy

char = 'abcdef'
char_ascii = [ord(c) for c in char if ord(c) > 100]

print char_ascii

# map根据指定的函数对序列进行映射
print map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])

char_ascii = list(filter(lambda c: c > 100, map(ord, char)))

print char_ascii