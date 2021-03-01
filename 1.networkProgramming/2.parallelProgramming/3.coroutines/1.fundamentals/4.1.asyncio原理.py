import time
import asyncio



def my_parallel_func(n_paral=10):
    """
    不是真正睡各自的时间，只是把最长的那个睡眠时间记录起来，然后让逐个较短时间的任务先去各自完成，给人的错觉是同时执行
        例如：
            a任务要睡3s，b任务要睡4s，他们共同睡的3s可以由a任务执行，然后b任务多出来的1s让其自己睡就好了，
            这样完成这两个时间的总时长是4s不是7s
    :param n_paral:
    :return:
    """
    def sleep_assist(n):
        print("before sleep {}s".format(n))
        yield time.time() + n
        print("end sleep {} s".format(n))

    def sleep(n):
        """
        yield from 是把该迭代器加到此程序中，每一次yield都相当于这个函数里面的yield
        相当于
            print("Start to activate sleep func n={}!".format(n))
            ->
            print("before sleep {}s".format(n))
            yield time.time() + n
            print("end sleep {} s".format(n))
            <-
            print("End sleep func n={}!".format(n))
        :param n:
        :return:
        """
        print("Start to activate sleep func n={}!".format(n))
        g = sleep_assist(n)
        yield from g
        print("End sleep func n={}!".format(n))

    g_list=[sleep(1+i*0.1) for i in range(n_paral)]
    time_list=[next(gi) for gi in g_list]
    time_dict={item[0]:item[1] for item in zip(time_list,g_list)}
    while time_dict:
        min_time=min(time_dict)
        time.sleep(min_time-time.time())
        try:
            next(time_dict[min_time])
        except StopIteration: pass
        del time_dict[min_time]

def parallel_fun(n_paral=10):
    async def sleep(n):
        print("Start to activate sleep func n={}!".format(n))
        print("before sleep {}s".format(n))
        await asyncio.sleep(n)
        print("end sleep {} s".format(n))
        print("End sleep func n={}!".format(n))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.wait(
            [sleep(1+i*0.1) for i in range(n_paral)]
        )
    )


if __name__ == '__main__':
    my_parallel_func(3)
    print("#######################")
    parallel_fun(3)
