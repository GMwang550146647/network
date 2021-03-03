
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
        2.基于管道 （pipeline.py文件）
            编码流程
                1.数据解析
                2.在item类中定义相关属性
                3.将解析的数据存储封装到item类型对象中
                4.item对象提交给管道
                5.管道类中process_item负责接收item对象，然后对item进行任何形式的持久化存储
                6.在配置文件中开启管道
    4.中间件
    5.全栈数据爬取操作
    6.分布式： redis（几乎不用）
    7.请求传参机制
    8.scrapy中合理应用selenium
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
import scrapy
from items import ScrapydemoItem

class ExampleSpider(scrapy.Spider):
    # 爬虫文件的唯一标识
    name = 'example'
    # 允许的域名
    # allowed_domains = ['example.com']
    # 起始的url列表：列表元素会被自动进行请求发送
    start_urls = ['https://dig.chouti.com']

    # 解析数据
    def parse(self, response):
        data_list=[]
        div_list = response.xpath('/html/body/main/div/div/div[1]/div/div[2]/div[1]')
        for div in div_list:
            # 产生的是Selector对象，我们解析获取的数据就是在对象中
            content = div.xpath('./div/div/div[1]/a/text()')[0].extract()
            item=ScrapydemoItem()
            item['content']=content
            data_list.append(content)
        return data_list
