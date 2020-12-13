from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def time_it(func, args):
    now = time.time()
    func(**args)
    return time.time() - now


class CalFib():
    def fib(self, n):
        if n <= 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def multi_processing_map(self, n_task=2000, depth=35):
        pp = ProcessPoolExecutor()
        result = [item for item in pp.map(self.fib, [depth for i in range(n_task)])]
        print("Multi Process Result:{}".format(result))
        return result

    def multi_threading_map(self, n_task=2000, depth=35):
        tp = ThreadPoolExecutor()
        result = [item for item in tp.map(self.fib, [depth for i in range(n_task)])]
        print("Multi Thread Result:{}".format(result))
        return result


if __name__ == '__main__':
    # 1.1.速度比较
    t_process = time_it(func=CalFib().multi_processing_map, args={'n_task': 6, 'depth': 30})
    t_thread = time_it(func=CalFib().multi_threading_map, args={'n_task': 6, 'depth': 30})
    print("Process: {}s".format(t_process))
    print("Thread: {}s".format(t_thread))
    print("________________THIS IS A SEPARATION LINE________________")
    # 1.2.速度比较
    t_process = time_it(func=CalFib().multi_processing_map, args={'n_task': 60, 'depth': 10})
    t_thread = time_it(func=CalFib().multi_threading_map, args={'n_task': 60, 'depth': 10})
    print("Process: {}s".format(t_process))
    print("Thread: {}s".format(t_thread))
    print("________________THIS IS A SEPARATION LINE________________")
    # 2.查看 是否使用多核
    # CalFib().multi_processing_map()
    # CalFib().multi_threading_map()
