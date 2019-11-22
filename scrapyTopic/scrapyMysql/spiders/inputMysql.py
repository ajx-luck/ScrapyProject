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
    start_urls = ['http://www.7t85.com']

    def parse(self, response):
        mingyan = response.css('a')

        item = ScrapymysqlItem()  # 实例化item类

        for v in mingyan:  # 循环获取每一条名言里面的：名言内容、作者、标签
            aa = v.xpath('@href').extract_first()
            if "areaid" in aa:
                item['areaid'] = aa  # 提取名言
                item['areaname'] = v.xpath('text()').extract_first()  # 提取标签
                yield item  # 把取到的数据提交给pipline处理




