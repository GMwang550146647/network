# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapydemoPipeline:
    fp = None
    """
    1.文件存储
    """
    def open_spider(self, spider):
        print('我只会在爬虫开始的时候执行一次')
        self.fp = open('pipeline_record.tsv', 'w')

    def close_spider(self, spider):
        print("我只会在爬虫结束的时候调用一次")
        self.fp.close()

    def process_item(self, item, spider):
        content = item['content']
        self.fp.write(content+'\n')
        return item

# class aaa():
#     def process_items(self,item,spider):
