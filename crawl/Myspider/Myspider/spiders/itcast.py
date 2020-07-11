# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast' #爬虫名
    allowed_domains = ['itcast.cn'] #允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] #最开始请求的URL地址

    # 处理start_url响应
    def parse(self, response):
        ret1 = response.xpath("//div[@class='main_mask']//h2/text()").extract()
        print(ret1)




