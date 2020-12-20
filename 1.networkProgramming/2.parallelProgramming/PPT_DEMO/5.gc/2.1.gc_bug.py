import gc
import time


class Teacher:
    def __init__(self):
        self.Stu = None

    def __del__(self):
        print('释放 Teacher实例')


class Student:
    def __init__(self):
        self.Tea = None

    def __del__(self):
        print('释放 Student实例')


def MethodTest():
    tea = Teacher()
    stu = Student()

    # 设置循环引用
    tea.Stu = stu
    stu.Tea = tea
    del tea
    del stu


if __name__ == '__main__':
    gc.enable()
    gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)

    MethodTest()

    print('开始内存回收...')
    _unreachable = gc.collect()
    print('无法到达的对象个数: %d' % _unreachable)
    print('内存泄露的对象个数:%d' % len(gc.garbage))

    # time.sleep(3)
    print('程序退出!')