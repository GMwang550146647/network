import gevent
import time
from threading import current_thread
"""
带有io的操作写在函数里面，提交函数给gevent
注意：
    request不行
"""


class GeventRun():

    def run_func(self, n_gevent=3, use_gevent=True):
        def func(i):
            print("Start: Thread {} exec func {}".format(current_thread().ident%100,i))
            # 这个不是gevent内置的规避io的操作，所以这个没用
            if use_gevent:
                gevent.sleep(0.1)
            else:
                time.sleep(0.1)
            print("End: Thread {} exec func {}".format(current_thread().ident % 100, i))

        g_list = []
        for i in range(n_gevent):
            gi = gevent.spawn(func, i=i)
            g_list.append(gi)
        # for gi in g_list: gi.join()
        gevent.joinall(g_list)

    def run(self):
        # 1.调用gevent内置的sleep,规避io
        self.run_func(use_gevent=True)
        print("________________THIS IS A SEPARATION LINE________________")
        # 2.调用python内置的sleep不能规避io
        self.run_func(use_gevent=False)
        print("________________THIS IS A SEPARATION LINE________________")
        # 3.monkey.patch_all()之后，python的sleep也能自动规避io
        from gevent import monkey
        monkey.patch_all(thread=False)
        self.run_func(use_gevent=True)
        print("________________THIS IS A SEPARATION LINE________________")
        # monkey.patch_all(thread=True)
        # self.run_func(use_gevent=False)


if __name__ == '__main__':
    GeventRun().run()
