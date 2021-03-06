"""
操作系统
    多道操作系统
        遇到io就切换
        提高cpu利用率
        进程间数据隔离
        时空复用：在同一个时间点上，多个程序执行着，一块内存条上面存储了多个进程数据
    分时操作系统
        时间分片
        时间片轮转
进程
    计算机中最小的资源分配单位：每一个程序运行起来的时候分配一些内存
    一个运行的程序
    操作系统中用pid唯一标识进程
    一般进程数不能超过cpu个数的两倍
并行和并发
    并行：多个cpu，各自在自己的cpu上执行多个程序
    并发：一个CPU，多个程序轮流执行
同步和异步
    同步：调用一个操作，要等待结果
    异步：调用一个操作，不等待结果
阻塞和非阻塞
    阻塞： CPU不工作
    非阻塞:CPU工作
同步阻塞
    一直等待结果，挂起自己，等一会再检查，不做其他事
    例如 input
同步非阻塞
    一直等待结果，不挂起自己
    例如 ret= eval("1+2+3-4") 没有发生阻塞事件
异步非阻塞
    不等待结果，不挂起自己，做其他事，这事做完了自然会通知
    例如-> start之后不需要返回的数据，让子进程自己执行完结束就好
异步阻塞
    不等待结果，做其他事情，再等待结果
    开启十个进程，异步，获取这个进程返回值，并且能做到谁先结束就获取谁的返回值，
    最先有后续动作执行的任务最后返回，导致其他后启动，先返回的任务阻塞
    例如-> start之后需要获取其返回的数据，但是各个子进程回来的顺序不依照start的顺序，所以是异步阻塞
例子解释:
    打电话给老板，问有没有计算机网络的书，
    同步： 一定要等到结果才罢休
        阻塞：  老板说我找找，就去找了一会儿，才回来回复，期间阻塞了
        非阻塞：老板瞬间回答了，没有阻塞
    异步： 不用等待老板结果，立刻挂断电话，老板有结果才回电话通知
        非阻塞：不等待老板的回复，做其他事情去了，一会再回来
        阻塞：
进程调度算法
    短作业优先
    先来先服务
    轮询
    多级反馈
"""