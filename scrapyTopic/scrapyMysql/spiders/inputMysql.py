# -*- coding: utf-8 -*-
"""
功能：本项目主要演示Scrapy数据存储MySQL具体操作；
运行环境：win7 64 + python3.6 + scrapy1.4 + mysql；
运行方式：进入scrapyMysql目录（scrapy.cfg目录)输入：

scrapy crawl inputMysql

项目详情：http://www.scrapyd.cn/jiaocheng/170.html；
注意事项：运行前请按项目详情创建好mysql数据库、表、字段；
创建时间：2018年1月30日14:40:50；
创建者：scrapy中文网（http://www.scrapyd.cn）；
"""
import scrapy
from scrapyMysql.items import ScrapymysqlItem  # 引入item


class InputmysqlSpider(scrapy.Spider):
    name = "inputMysql"
    allowed_domains = ['7t85.com']
    start_urls = ['http://www.7t85.com/ShowInfo.asp?id=106589']

    def parse(self, response):

        item = ScrapymysqlItem()  # 实例化item类
        topic = response.css('.ff660016')
        t = topic[0]

        atxt = t.xpath('string(..)').extract_first().strip('\t').strip()
        tx1 = "".join(atxt.split())
        arrs = tx1.split('：')
        length = len(arrs)

        item['title'] = arrs[1][:-4]
        item['category'] = arrs[2][:-4]
        addrs = arrs[3][:-4].split("-")
        item['provice'] = addrs[0]
        item['city'] = addrs[1]
        item['address'] = arrs[4][:-4]
        item['infocome'] = arrs[5][:-4]
        item['missnumber'] = arrs[6][:-4]
        item['missage'] = arrs[7][:-4]
        item['missquality'] = arrs[8][:-4]
        item['missappearance'] = arrs[9][:-4]
        item['sextype'] = arrs[10][:-4]
        item['price'] = arrs[11][:-4]
        item['bustime'] = arrs[12][:-4]
        item['env'] = arrs[13][:-4]
        item['safety'] = arrs[14][:-4]
        item['contact'] = arrs[15][:-4]
        item['evaluate'] = arrs[16][:-4]

        yield item  # 把取到的数据提交给pipline处理


