"""
scrapy使用
    pySpider
框架
    具有很强通用性的项目模板
scrapy集成的功能
    1.高性能数据解析操作（xpath）
    2.高性能数据下载
    3.高性能持久化存储
        1.基于终端指令
            只能将parse方法的返回值存储到硬盘文件中 csv 或者json （不能txt）
                scrapy crawl example -o save_file.csv
                settings
                    不遵从robots协议
                    UA伪装
                    LOG_LEVEL='ERROR'
                    LOG_FILE='log.txt'
                    RETRY_ENABLED = True  ->重试
                    COOKIES_ENABLED= False ->不存储COOKIE
                    DOWNLOAD_TIMEOUT =10   ->超时时间10s

        2.基于管道 （pipeline.py文件）
            编码流程
                1.数据解析
                2.在item类中定义相关属性
                3.将解析的数据存储封装到item类型对象中
                4.item对象提交给管道
                5.管道类中process_item负责接收item对象，然后对item进行任何形式的持久化存储
                6.在配置文件中开启管道
            细节：
                1.管道文件中的一个管道类表示将数据存储到某形式的平台中
                2.如果管道文件中定义了多个管道类，爬虫提交的item会给到优先级最高的管道类
                3.process_item 方法的实现 return item 操作表示 优先级高的管道类将 数据传到优先级低的管道类中(优先值越小优先度越高)
    4.中间件
        爬虫中间件

        下载中间件
            作用：
                批量拦截所有请求和响应
            为什么拦截
                篡改请求对应的ip（代理）
                修改请求对应的ip（代理）
            为什么拦截响应
                篡改相应数据，篡改响应对象
    5.全栈数据爬取操作
        基于Spider父类进行全站数据爬取
            全站数据爬取：将所有野马对应页面数据爬取
            手动请求发送(get 请求)
                yield scrapy.Request(url,callback)
            手动请求发送（post请求）
                yield scrapy.FormRequest(url,formdata,callback):formdata是请求参数
    6.分布式（几乎不用）： redis
    7.请求传参机制
    8.scrapy中合理应用selenium

scrapy核心组件
                 调度器
                  ↑ ↓
                  ↑ ↓                                    互联网
                  ↑ ↓                                    ↗ ↙
                  ↑ ↓                                    ↗ ↙
     管道→→→→→→→→→→引→→→→→下载 →→→→→下载器(异步Twisted.whl)↗ ↙
        ←←←←←←←←←←擎←←←←←中间件←←←←←
                  ↑ ↓
                  ↑ ↓
                爬虫中间件
                  ↑ ↓
                  ↑ ↓
                 Spider
    1.引擎
        处理整个系统数据流处理，触发事务（框架核心）
    2.调度器
        用来接收引擎发过来的请求，丢到队列里，引擎再次请求的时候返回，想象成一个URL的优先队列，去决定下一个要抓取的网址是什么，同时去重
    3.管道
        负责爬虫从网页中抽取实体，持久化实体，验证实体有效性，清除不需要的页面信息，被爬虫解析之后，发送到Pipeline中根据次序处理
    4.Spider
        网页中提取自己需要的信息（Item)，用户也可以提取出链接，让scrapy抓取下一个页面
    5.下载器
        用于下载网页内容，讲网页内容返回给spider（建立在twisted高效异步模型中)
"""
"""
1.启动项目
    scrapy startproject scrapydemo
2.创建爬虫文件
    cd scrapydemo
    scrapy genspider example www.xxx.com
3.执行爬虫
    scrapy crawl example
"""