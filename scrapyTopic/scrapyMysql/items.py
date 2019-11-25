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


class ScrapymysqlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标签字段
    category = scrapy.Field()  # 名言内容
    provice = scrapy.Field()
    city = scrapy.Field()
    address = scrapy.Field()
    infocome = scrapy.Field()
    missnumber = scrapy.Field()
    missage = scrapy.Field()
    missquality = scrapy.Field()
    missappearance = scrapy.Field()
    sextype = scrapy.Field()
    price = scrapy.Field()
    bustime = scrapy.Field()
    env = scrapy.Field()
    safety = scrapy.Field()
    contact = scrapy.Field()
    evaluate = scrapy.Field()
    pass
