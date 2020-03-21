# encoding: utf-8

'''
    sorted 与 list.sort()
    sorted: 复制一份列表，排序支持逆序，排序的算法是稳定的排序
    list.sort(): 就地排序

'''

alph = ['a', 'c', 'b', 'd', 'z']

a = sorted(alph)

b = sorted(alph, reverse=True)
bkey = sorted(alph, key=len, reverse=True)
c = list.sort(alph)                 # 对alph就地排序, 没有返回值

print '\n'.join(map(lambda x: str(x), [a, b, bkey, c, alph]))

hystack = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
needle = [1, 4, 11, 20]
# python3
# import bisert
# for n in needle:
#    index = bisert.bisert(hystack, n)  # bisert/bisert_left/bisert_right
# bisert.insort(seq, item) 把item插入seq, 并保持seq的升序排序

'''
    双向队列, 先进先出
'''
from collections import deque
dq = deque(range(10), maxlen=10)
print dq
dq.rotate(3)             # rotate:  deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
print 'rotate: ', dq     # 右边3个移到左边
dq.rotate(-4)            # rotate:  deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
print 'rotate: ', dq     # 左边4个移到右
dq.appendleft('10')      # deque(['10', 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
print dq
dq.extend(['11','12', '13'])  # deque([3, 4, 5, 6, 7, 8, 9, '11', '12', '13'], maxlen=10)
print dq
dq.extendleft(['x', 'y'])  # deque(['y', 'x', 3, 4, 5, 6, 7, 8, 9, '11'], maxlen=10) 注意，按书序从左边进入队列
print dq










