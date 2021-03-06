# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
import scrapy


class PhotoPipeline:
    def open_spider(self, spider):
        print('我只会在爬虫开始的时候执行一次')
        self.fp = open('data/pipeline_record.tsv', 'w')

    def close_spider(self, spider):
        print("我只会在爬虫结束的时候调用一次")
        self.fp.close()

    def process_item(self, item, spider):
        content = {
            'img_src': item['img_src'],
        }
        content = json.dumps(content)
        self.fp.write(content + '\n')
        print("File Inserted : {}".format(content))
        return item  # 会继续把数据传到下一个优先级的PipeLine -> mysqlPipeLine


from scrapy.pipelines.images import ImagesPipeline


class PhotoPipeline_photo(ImagesPipeline):

    def get_media_requests(self, item, info):
        '''
        对媒体资源进行请求下载，参数item就是接收到的爬虫类提交的item对象
        '''
        yield scrapy.Request(item['img_src'])

    def file_path(self, request, response=None, info=None):
        '''
        指明数据存储路径
        '''
        return request.url.split('/')[-1]

    def item_completed(self, results, item, info):
        '''
        完成之后还要做什么操作
        '''
        return item
