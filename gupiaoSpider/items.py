# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GupiaospiderItem(scrapy.Item):
    # define the fields for your item here like:
    gpcode = scrapy.Field()    # 0：”大秦铁路”，股票名字；
    kaipanjia=scrapy.Field() # 1：”27.55″，今日开盘价；
    zuorishoupanjia=scrapy.Field() # 2：”27.25″，昨日收盘价；
    dangqianjia=scrapy.Field() # 3：”26.91″，当前价格；
    jinrizuigaojia=scrapy.Field() # 4：”27.55″，今日最高价；
    jinrizuidijia=scrapy.Field() # 5：”26.20″，今日最低价；
    jingbuy1=scrapy.Field() # 6：”26.91″，竞买价，即“买一”报价；
    jingsale1=scrapy.Field() # 7：”26.92″，竞卖价，即“卖一”报价；
    chengjiaogupiaoshu=scrapy.Field() # 8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
    chengjiaojine=scrapy.Field() # 9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
    buygushu1=scrapy.Field() # 10：”4695″，“买一”申请4695股，即47手；
    buybaojia1=scrapy.Field() # 11：”26.91″，“买一”报价；
    buygushu2 = scrapy.Field()# 12：”57590″，“买二”
    buybaojia2 = scrapy.Field()# 13：”26.90″，“买二”
    buygushu3=scrapy.Field()# 14：”14700″，“买三”
    buybaojia3 = scrapy.Field()    # 15：”26.89″，“买三”
    buygushu4 = scrapy.Field()# 16：”14300″，“买四”
    buybaojia4 = scrapy.Field()# 17：”26.88″，“买四”
    buygushu5 = scrapy.Field()# 18：”15100″，“买五”
    buybaojia5 = scrapy.Field()    # 19：”26.87″，“买五”
    salegushu1=scrapy.Field()# 20：”3100″，“卖一”申报3100股，即31手；
    salebaojia1=scrapy.Field()# 21：”26.92″，“卖一”报价
    salegushu2 = scrapy.Field()
    salebaojia2 = scrapy.Field()
    salegushu3 = scrapy.Field()
    salebaojia3 = scrapy.Field()
    salegushu4 = scrapy.Field()
    salebaojia4 = scrapy.Field()
    salegushu5 = scrapy.Field()
    salebaojia5 = scrapy.Field()
    # (22, 23), (24, 25), (26, 27), (28, 29)
    # 分别为“卖二”至“卖五的情况”
    riqi=scrapy.Field()# 30：”2008 - 01 - 11″，日期；
    shijian=scrapy.Field() # 31：”15:05:32″，时间；

# #定义原始Item
# class Product(scrapy.Field):
#     name=scrapy.Field()
# #扩展Item
# # 您可以通过继承原始的Item来扩展item(添加更多的字段或者修改某些字段的元数据)。
# class DiscountedProduct(Product):
#     discount_percent=scrapy.Field(serializer=str)
#     discount_expiration_date=scrapy.Field()
#
#
# # 您也可以通过使用原字段的元数据,添加新的值或修改原来的值来扩展字段的元数据:
# # 这段代码在保留所有原来的元数据值的情况下添加(或者覆盖)了 name 字段的 serializer 。
# class SpecificProduct(Product):
#     name=scrapy.Field(Product.fields['name'],serializer=my_serializer)