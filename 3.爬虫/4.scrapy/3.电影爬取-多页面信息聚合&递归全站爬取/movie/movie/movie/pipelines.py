# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MoviePipeline:
    def open_spider(self, spider):
        print('我只会在爬虫开始的时候执行一次')
        self.fp = open('data/pipeline_record.tsv', 'w')

    def close_spider(self, spider):
        print("我只会在爬虫结束的时候调用一次")
        self.fp.close()

    def process_item(self, item, spider):
        content = '\t'.join([item.get('title',' '), item.get('desc_url'," "), item.get('video_url',' '), str(item.get('desc',' '))])

        self.fp.write(content + '\n')
        print("File Inserted : {}".format(content))
        return item  # 会继续把数据传到下一个优先级的PipeeLine -> mysqlPipeLine
