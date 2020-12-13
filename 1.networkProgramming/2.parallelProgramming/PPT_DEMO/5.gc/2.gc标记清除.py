import sys
import gc
import sys

class LabelRemoveRun():
    def label_remove_success(self):
        a = [1]
        b = [2]
        a.append(b)
        b.append(a)
        # 此时a和b之间存在循环引用
        print('a count:', sys.getrefcount(a))  # 结果应该是3
        print('b count:', sys.getrefcount(b))  # 结果应该是3
        del a
        del b
        # 删除了变量名a，b到对象的引用，此时引用计数应该减为1，即只剩下互相引用了
        try:
            sys.getrefcount(a)
        except Exception as err:
            print('a is invalid')
        # 此时，原来a指向的那个对象引用不为0，python不会自动回收它的内存空间
        # 但是我们又没办法通过变量名a来引用它了，这就导致了内存泄露
        unreachable_count = gc.collect()
        print("Unreachable: {}".format(unreachable_count))
        # gc.collect()专门用来处理这些循环引用，返回处理这些循环引用一共释放掉的对象个数。这里返回是2

    def run(self):
        self.label_remove_success()

if __name__ == '__main__':
    LabelRemoveRun().run()
