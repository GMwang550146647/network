"""
组件名称	对应类名	    功能描述
日志器	Logger	    提供了应用程序可一直使用的接口（就是输出的目标文件位置）
处理器	Handler	    将logger创建的日志记录发送到合适的目的输出（处理器（handler）还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作）
过滤器	Filter	    提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
格式器	Formatter	决定日志记录的最终输出格式
"""

"""

详情见
https://www.cnblogs.com/Nicholas0707/p/9021672.html
"""