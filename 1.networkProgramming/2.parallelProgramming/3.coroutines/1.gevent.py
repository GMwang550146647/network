import gevent
import time
"""
带有io的操作写在函数里面，提交函数给gevent
注意：
    request不行
"""



def run_func_gevent(n_gevent=10):
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

def run_func(n_gevent=10):
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

if __name__ == '__main__':
    #规避io
    run_func_gevent()
    #不能规避io
    run_func()