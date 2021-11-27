import math


def square():
    return 0


class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Point(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def square(self):
        return math.pi * self.r ** 2

    def contains(self, point):
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.r ** 2

    def __contains__(self, point):
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.r ** 2


# проверка
c = Circle(1, 1, 15)
p1 = Point(3, 11)
p2 = Point(-5, -16)
print(c.contains(p1))
print(p1 in c)
print(c.contains(p2))
print(p2 in c)
