from math import sqrt

class PointError(Exception):
    pass

class Point:
    def __init__(self, *x):  # Accept exactly two parameters
        if len(x) != 2:
            raise PointError('Need two coordinates, point not created.')
        self.x, self.y = x

    def __repr__(self):  # Return a string representation of the Point object
        return (f'Point({self.x}, {self.y})')

    def __str__(self):  # Return a string for print() function
        return f'Point of x-coordinate {self.x} and y-coordinate {self.y}'
class TriangleError(Exception):
    pass
class Triangle:
    def __init__(self, *, point_1, point_2, point_3):
        self.point_1 = point_1 
        self.point_2 = point_2 
        self.point_3 = point_3
        self.modified = False  # 添加一个标志来跟踪是否成功修改了三角形
        if not self._validate_points():
            raise TriangleError('Incorrect input, triangle not created.')
        self.modified = True

    def _validate_points(self):
        # 检查是否所有点都是 Point 实例并且不共线
        return (all(isinstance(point, Point) for point in (self.point_1, self.point_2, self.point_3))
                and not self.check_collinear())

    def check_collinear(self):
        dx1 = self.point_2.x - self.point_1.x
        dy1 = self.point_2.y - self.point_1.y
        dx2 = self.point_3.x - self.point_1.x
        dy2 = self.point_3.y - self.point_1.y
        return dx1 * dy2 == dy1 * dx2
    @property
    def perimeter(self):
            side_a = sqrt((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2)
            side_b = sqrt((self.point_2.x - self.point_3.x) ** 2 + (self.point_2.y - self.point_3.y) ** 2)
            side_c = sqrt((self.point_3.x - self.point_1.x) ** 2 + (self.point_3.y - self.point_1.y) ** 2)
            return side_a + side_b + side_c
    @property
    def area(self):
            s = self.perimeter / 2
            side_a = sqrt((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2)
            side_b = sqrt((self.point_2.x - self.point_3.x) ** 2 + (self.point_2.y - self.point_3.y) ** 2)
            side_c = sqrt((self.point_3.x - self.point_1.x) ** 2 + (self.point_3.y - self.point_1.y) ** 2)
            area = sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
            return area

    def change_point_or_points(self, *, point_1=None, point_2=None, point_3=None):
        original_points = self.point_1, self.point_2, self.point_3
        if point_1:
            self.point_1 = point_1
        if point_2:
            self.point_2 = point_2
        if point_3:
            self.point_3 = point_3
        
        if not self._validate_points():
            # 如果修改后的点共线或者不是 Point 实例，恢复原始点
            self.point_1, self.point_2, self.point_3 = original_points
            print('Incorrect input, triangle not modified.')
        else:
            self.modified = True