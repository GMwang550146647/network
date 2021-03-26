class Point:
    x = 100

    def __new__(cls, *args, **kwargs):
        '''
        构造函数：
            该函数出现在构建类对象之前，所以没有self
        '''
        print("args:{},kwargs:{}".format(args, kwargs))
        return super().__new__(cls)

    def __init__(self, x, y):
        '''
        初始化函数：

        '''
        self.x = x
        self.y = y
        print('__dict__ of object:', self.__dict__)
        print('__dict__ of class:', self.__class__.__dict__)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


if __name__ == '__main__':
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(p1.__class__.x)
    print(Point.calculate_distance(p1, p2))
