# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class MoviePipeline:
    """
    mysql 配置
        create database spider default character set utf8;
        use spider
        create table moviedata (title varchar(200), desc_url varchar(40), video_url varchar(100), desc_detail varchar(30000));
    """
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='gmwang', db='spider')
        self.cursor = self.conn.cursor()
        # 1.删除之前数据
        try:
            sql = """delete from moviedata;"""
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as err:
            print("Delete from Sql Failure")
            self.conn.rollback()

    def process_item(self, item, spider):
        # 2.写入新数据
        if item.__class__.__name__ == 'MovieItemPart1':

            sql = '''insert into moviedata values ('%s','%s','%s','%s');''' % (
                item['title'], item['desc_url'], ' ', ' ')
            try:
                self.cursor.execute(sql)
                print(sql)
                print('Mysql Inserted {}'.format(item))
                self.conn.commit()
            except Exception as err:
                print(err)
                self.conn.rollback()
        elif item.__class__.__name__ == 'MovieItemPart2':
            sql = '''update moviedata set desc_detail='%s',video_url='%s' where title='%s';''' % (
                item['desc_detail'], item['video_url'], item['title'])
            try:
                self.cursor.execute(sql)
                print(sql)
                print('Mysql Updated {}'.format(item))
                self.conn.commit()
            except Exception as err:
                print(err)
                self.conn.rollback()
        else:
            print("Error!!!!!!!!!!!!!!!!!!!!!!")
        return item  # 会继续把数据传到下一个优先级的PipeLine -> redisPipeline

    def close_spider(self, spider):
        self.conn.close()
