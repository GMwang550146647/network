import scrapy
import json
from ..items import LotteryItem
import datetime
from redis import Redis

class LotteryScrawlerSpider(scrapy.Spider):
    conn = Redis(host='127.0.0.1', port=6379)
    name = 'lottery_scrawler'
    # allowed_domains = ['www.xxx.com']
    date_start = '2000-01-01'
    date_end = datetime.datetime.now().strftime('%Y-%m-%d')
    url_format = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart={}&dayEnd={}&pageNo='.format(
        date_start, date_end)
    start_urls = [url_format]
    current_page = 1

    def parse(self, response):
        details = response.json()
        lottery_items = details.get('result', [])
        for lottery_item_i in lottery_items:

            ex = self.conn.sadd('lottery_codes', lottery_item_i['code'])
            if ex == 1:
                print("捕获到最新消息: {}".format(lottery_item_i['code']))
                lottery_item = LotteryItem()
                lottery_item['code'] = lottery_item_i.get('code', '')
                lottery_item['date'] = lottery_item_i.get('date', '')
                lottery_item['red'] = lottery_item_i.get('red', '')
                lottery_item['sales'] = lottery_item_i.get('sales', '')
                lottery_item['poolmoney'] = lottery_item_i.get('poolmoney', '')
                lottery_item['content'] = lottery_item_i.get('content', '')
                lottery_item['prizegrades'] = json.dumps(lottery_item_i.get('prizegrades', ''))
                yield lottery_item
            else:
                print("老消息啦 : {}".format(lottery_item_i['code']))
        all_pages = details.get('pageCount', 1)
        self.current_page += 1
        if self.current_page <= all_pages:
            yield scrapy.Request(self.url_format + str(self.current_page), callback=self.parse)
