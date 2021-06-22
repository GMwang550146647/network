'''
3.Pool：
    如果要启用大量子进程，利用进程池方式批量创建子进程

'''
from multiprocessing import Pool
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


print('Parent process %s.' % os.getpid())
p = Pool()  #3.1.创建进程池，可以自己设置最大线程数，例如p=Pool(8)
for i in range(5):
    p.apply_async(long_time_task, args=(i,))  #3.2.进程池中加入任务
print('Waiting for all subprocesses done...')
p.close()  #3.3.对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
p.join()
print('All subprocesses done.')