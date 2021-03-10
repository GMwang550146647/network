# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class LeetcodePipeline:
    attrs=["index","title","pass_rate","difficulty","desc_url"]
    def open_spider(self, spider):
        print('我只会在爬虫开始的时候执行一次')
        self.fp = open('data/pipeline_record.tsv', 'w')

    def close_spider(self, spider):
        print("我只会在爬虫结束的时候调用一次")
        self.fp.close()

    def process_item(self, item, spider):
        content=[item.get(attri,"None") for attri in self.attrs]
        content='\t'.join(content)
        self.fp.write(content + '\n')
        with open('data/problems/{}.{}_{}.txt'.format(item['index'],item['difficulty'],item['title']) ,'w') as f:
            try:
                f.write(item['desc'])
            except:
                f.write('Content Locked!')
        print("File Inserted : {}".format(content))
        return item  # 会继续把数据传到下一个优先级的PipeLine -> mysqlPipeLine