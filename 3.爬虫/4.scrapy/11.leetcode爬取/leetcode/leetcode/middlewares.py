# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import re
import time
import numpy as np
from scrapy import signals
from scrapy.http import HtmlResponse
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium.webdriver.support.ui import Select


class LeetcodeSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LeetcodeDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def tell_true(self, url, patterns):
        qualified = [len(re.findall(patterni, url)) > 0 for patterni in patterns]
        qualified = np.array(qualified).any()
        return qualified

    def process_response(self, request, response, spider):
        if self.tell_true(request.url, spider.problemset_url_pattern):
            print('2',request.url)
            driver = spider.web_driver
            driver.get(request.url)
            select = Select(driver.find_elements_by_xpath(
                '//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table//tr/td/span/select')[0])
            select.select_by_visible_text("全部")  # 选择text="o3"的值，即在下拉时我们可以看到的文本
            page_source = driver.page_source
            new_reponse = HtmlResponse(url=request.url, body=page_source, encoding='utf-8', request=request)
            return new_reponse
        elif self.tell_true(request.url, spider.detail_url_pattern):
            print('1',request.url)
            driver = spider.web_driver
            driver.get(request.url)
            page_source = driver.page_source
            new_reponse = HtmlResponse(url=request.url, body=page_source, encoding='utf-8', request=request)
            return new_reponse
        else:
            print('3',request.url)
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
