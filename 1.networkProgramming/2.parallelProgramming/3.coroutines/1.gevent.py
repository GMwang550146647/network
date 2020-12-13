import gevent
import time
"""
带有io的操作写在函数里面，提交函数给gevent
注意：
    request不行
"""

class GeventRun():

    def run_func_gevent(self,n_gevent=10):
        def func_gevent(i):
            print("start func_gevent {}".format(i))
            # 这个是gevent的自定义规避io的操作
            gevent.sleep(1)
            print('end func_gevent {}'.format(i))
        g_list = []
        for i in range(n_gevent):
            gi = gevent.spawn(func_gevent, i=i)
            g_list.append(gi)
        # for gi in g_list: gi.join()
        gevent.joinall(g_list)

    def run_func(self,n_gevent=10):
        def func(i):
            print("start func {}".format(i))
            # 这个不是gevent内置的规避io的操作，所以这个没用
            time.sleep(1)
            print('end func {}'.format(i))
        g_list = []
        for i in range(n_gevent):
            gi = gevent.spawn(func, i=i)
            g_list.append(gi)
        # for gi in g_list: gi.join()
        gevent.joinall(g_list)
    def run(self):
        # 1.规避io
        self.run_func_gevent()
        # 2.不能规避io
        self.run_func()
        # 3.自动规避io
        from gevent import monkey
        monkey.patch_all()
        self.run_func()
if __name__ == '__main__':
    GeventRun().run()