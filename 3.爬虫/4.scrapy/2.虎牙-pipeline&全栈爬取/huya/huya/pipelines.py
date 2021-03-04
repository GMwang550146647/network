# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HuyaPipeline:
    def open_spider(self, spider):
        print('我只会在爬虫开始的时候执行一次')
        self.fp = open('data/pipeline_record.tsv', 'w')

    def close_spider(self, spider):
        print("我只会在爬虫结束的时候调用一次")
        self.fp.close()

    def process_item(self, item, spider):
        content = '\t'.join([item['title'], item['url'], item['likes']])
        self.fp.write(content + '\n')
        print("File Inserted : {}".format(item))
        return item  # 会继续把数据传到下一个优先级的PipeeLine -> mysqlPipeLine


import pymysql
from redis import Redis


class mysqlPipeLine(object):
    """
    mysql 配置
        create database spider default character set utf8;
        use spider
        create table huyadata(title varchar(200), url varchar(40), likes int);
    """
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='gmwang', db='spider')
        self.cursor = self.conn.cursor()
        # 1.删除之前数据
        try:
            sql = """delete from huyadata;"""
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as err:
            print("Delete from Sql Failure")
            self.conn.rollback()

    def process_item(self, item, spider):
        # 2.写入新数据
        sql = '''insert into huyadata values ("%s","%s","%s");''' % (item['title'], item['url'], item['likes'])

        try:
            self.cursor.execute(sql)
            print('Mysql Inserted {}'.format(item))
            self.conn.commit()
        except Exception as err:
            print(err)
            self.conn.rollback()

        return item  # 会继续把数据传到下一个优先级的PipeLine -> redisPipeline

    def close_spider(self, spider):
        self.conn.close()


from rediscluster import RedisCluster


class RedisPipeLine(object):
    conn = None
    data_tag = 'huyaList'

    def open_spider(self, spider):
        try:
            startup_nodes = [
                {'host': '127.0.0.1', 'port': 6371},
                {'host': '127.0.0.1', 'port': 6372},
                {'host': '127.0.0.1', 'port': 6373},
            ]
            self.conn = RedisCluster(
                startup_nodes=startup_nodes,
                decode_responses=True,
                # password=None
            )
            self.conn.delete(self.data_tag)

        except Exception as e:
            print("Cluster Connection Error:{}".format(str(e)))

    def process_item(self, item, spider):
        self.conn.lpush(self.data_tag, item)
        print('Redis Inserted {}'.format(item))
        return item

    def close_spider(self, spider):

        self.check_save()

    def check_save(self):
        try:
            startup_nodes = [
                {'host': '127.0.0.1', 'port': 6371},
                {'host': '127.0.0.1', 'port': 6372},
                {'host': '127.0.0.1', 'port': 6373},
            ]
            r = RedisCluster(
                startup_nodes=startup_nodes,
                decode_responses=True,
                # password=None
            )
            all_data = r.lrange('huyaList', 0, -1)
            with open('data/redis_list.tsv', 'w') as f:
                f.write('\n'.join(all_data))

        except Exception as e:
            print("Cluster Connection Error:{}".format(str(e)))


if __name__ == '__main__':
    RedisPipeLine().check_save()
