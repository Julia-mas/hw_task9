class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        tmp = Point(
            self.x + other.x,
            self.y + other.y
        )
        return tmp

    def __sub__(self, other):
        tmp = Point(
            self.x - other.x,
            self.y - other.y
        )
        return tmp

    @staticmethod
    def check_data(*args):
        for arg in args:
            if type(arg) == int:
                return True
            else:
                return False

    def get_coordinates(self):
        return self.x, self.y

    def change_position(self, x, y):
        self.x = x
        self.y = y

    def new_coordinates(self, x, y):
        if Point.check_data(x, y):
            self.change_position(x, y)


pr = Point()
pr_1 = Point(12, 33)
pr_2 = Point(7, 10)
pr_3 = Point(20, 10)
print(pr_1.x, pr_1.y)
print(pr_2.x, pr_2.y)

res = pr_1 + pr_2
res_2 = pr_1 - pr_2
print(res.x, res.y)
print(res_2.x, res_2.y)


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        if Point.check_data(x1, y1, x2, y2, x3, y3):
            self.p1 = Point(x1, y1)
            self.p2 = Point(x2, y2)
            self.p3 = Point(x3, y3)

    def get_points(self):
        (x1, y1), (x2, y2), (x3, y3) = (point.get_coordinates() for point in self.__dict__.values())
        return x1, y1, x2, y2, x3, y3

    @staticmethod
    def is_triangle(self):
        x1, y1, x2, y2, x3, y3 = self.get_points()
        if ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 + ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5 > \
                ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5 \
                or ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5 + ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5 > (
                (x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 \
                or ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5 + ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 > (
                (x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5:
            return True
        else:
            return False

    def get_perimeter(self):
        x1, y1, x2, y2, x3, y3 = self.get_points()
        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
        return round(a + b + c, 2)

    def get_area(self):
        x1, y1, x2, y2, x3, y3 = self.get_points()
        return abs(((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) * 0.5)

    def change_apex(self, apex, x, y):
        if apex in self.__dict__:
            self.__dict__[apex].new_coordinates(x, y)
        else:
            return AttributeError(f'Wrong apex {apex}')


tr = Triangle(pr_1.x, pr_1.y, pr_2.x, pr_2.y, pr_3.x, pr_3.y)
print(tr.get_perimeter())
print(tr.get_area())
print(tr.is_triangle(tr))
