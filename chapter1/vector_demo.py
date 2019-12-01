# coding: utf-8

from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 定义了打印的格式，如果没有打印对象时，可能会是<Vector object at 0x10xxxxxx>
    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # bool() 调用这个方法
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


if __name__ == "__main__":
    print Vector(1, 2)
    print Vector(1, 2) * 10

    print str(Vector(1, 2))
    Vector(1, 2)

