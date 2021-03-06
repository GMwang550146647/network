from scrapy.cmdline import execute
import os
import sys
"""
1. pip install scrapy-redis
2. scrapy startproject projectName
3. scrapy genspider -t crawl spiderName www.xxx.com
4. 修改爬虫类
    导包： from scrapy_redis.spiders import RedisSpider
    修改当前爬虫类的父类为RedisCrawlSpider
    allowed_domains 和 start_urls 删除
    添加新属性redis_key='fbsQueue'，表示是共享调度器名称
    编写爬虫类的常规操作
5.指定pipeline
    SPIDER_MIDDLEWARES = {
   'movie.middlewares.RedisPipeline': 543,
}
6.指定调度器（settings)
    # 增加了一个去重容器类的配置，作用使用Redis的set集合来存储请求的指纹数据，从而实现请求去重的持久化
    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
    # 使用scrapy-redis组建自己的调度器
    SCHEDULE = "scrapy_redis.scheduler.Scheduler"
    # 配置调度器是否需要持久化，爬虫结束后，要不要清空Redis中请求队列和去重的set，如果True表示持久化存储，不清空，否则清空
    SCHEDULE_PERSIST = True
7.指定redis数据库
    REDIS_HOST='127.0.0.1'
    REDIS_PORT='6379'
    #PS 还需要：
        # 关闭默认绑定 #bind 127.0.0.1
        # 关闭保护模式 #protected-mode no
8.启动
    服务端
        redis-server xxx.config
        redis-cli -p PORT
    向调度器扔入一个原始的url
        redis中
            lpush fbsQueue 'http://www.4567kan.com/frim/index1.html'
        查看结果：
            keys *
            llen movie_crawlSpider:items
"""
if __name__ == '__main__':
    os.makedirs('data',exist_ok=True)
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    #使用pipeline
    # execute(['scrapy','crawl','movie_crawler'])
    execute(['scrapy','runspider','movie_crawlSpider.py'])
    #使用文件output
    # execute(['scrapy','crawl','huya_crawler','-o','file_record.csv'])