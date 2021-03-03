# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapydemoPipeline:
    fp = None

    def open_spider(self, spider):
        print('我只会在爬虫开始的时候执行一次')
        self.fp = open('record.tsv', 'w')

    def process_item(self, item, spider):
        content = item['content']
        self.fp.write(content)
        return item

    def close_spider(self, spider):
        print("我只会在爬虫结束的时候调用一次")
        self.fp.close()

# class aaa():
#     def process_items(self,item,spider):
