"""
1.logging.basicConfig(**kwargs)
用于指定“要记录的日志级别”、“日志格式”、“日志输出位置”、“日志文件的打开模式”等信息
1.1.具体参数如下所示：

参数名称                	描述
filename	指定日志输出目标文件的文件名（可以写文件名也可以写文件的完整的绝对路径，写文件名日志放执行文件目录下，写完整路径按照完整路径生成日志文件），指定该设置项后日志信心就不会被输出到控制台了
filemode	指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效
format	    指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序。logging模块定义的格式字段下面会列出。
datefmt	    指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效
level	    指定日志器的日志级别
stream	    指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常
style	    Python 3.2中新添加的配置项。指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%'
handlers	Python 3.3中新添加的配置项。该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常。


1.2.用于format的字段：

字段/属性名称	使用格式	描述
asctime	        %(asctime)s	    将日志的时间构造成可读的形式，默认情况下是‘2016-02-08 12:00:00,123’精确到毫秒
name	        %(name)s	    所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
filename	    %(filename)s	调用日志输出函数的模块的文件名； pathname的文件名部分，包含文件后缀
funcName	    %(funcName)s	由哪个function发出的log， 调用日志输出函数的函数名
levelname	    %(levelname)s	日志的最终等级（被filter修改后的）
message	        %(message)s	    日志信息， 日志记录的文本内容
lineno	        %(lineno)d	    当前日志的行号， 调用日志输出函数的语句所在的代码行
levelno	        %(levelno)s	    该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
pathname	    %(pathname)s	完整路径 ，调用日志输出函数的模块的完整路径名，可能没有
process	        %(process)s	    当前进程， 进程ID。可能没有
processName	    %(processName)s	进程名称，Python 3.1新增
thread	        %(thread)s	    当前线程， 线程ID。可能没有
threadName	    %(thread)s	    线程名称
module	        %(module)s	    调用日志输出函数的模块名， filename的名称部分，不包含后缀即不包含文件后缀的文件名
created	        %(created)f	    当前时间，用UNIX标准的表示时间的浮点数表示； 日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
relativeCreated	%(relativeCreated)d	输出日志信息时的，自Logger创建以 来的毫秒数； 日志事件发生的时间相对于logging模块加载时间的相对毫秒数
msecs	        %(msecs)d	    日志事件发生事件的毫秒部分。logging.basicConfig()中用了参数datefmt，将会去掉asctime中产生的毫秒部分，可以用这个加上
"""

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



"""
2.创建特定类型的日志
logging.debug(msg, *args, **kwargs)	创建一条严重级别为DEBUG的日志记录
logging.info(msg, *args, **kwargs)	创建一条严重级别为INFO的日志记录
logging.warning(msg, *args, **kwargs)	创建一条严重级别为WARNING的日志记录
logging.error(msg, *args, **kwargs)	创建一条严重级别为ERROR的日志记录
logging.critical(msg, *args, **kwargs)	创建一条严重级别为CRITICAL的日志记录
logging.log(level, *args, **kwargs)	创建一条严重级别为level的日志记录
"""
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")