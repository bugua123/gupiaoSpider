# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
import logging
from scrapy.conf import settings
import sys

reload(sys)
sys.setdefaultencoding('utf8')
class PipelineToJson(object):
    def __init__(self):
        self.f=open('gp.json','w')
    def process_item(self,item,spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"  # 确保中文显示正常

        self.f.write(content)
        return item
    def close_spider(self,spider):
        self.f.close()

class GupiaospiderPipeline(object):
    def __init__(self):
        host = settings['MYSQL_HOST']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        c = settings['CHARSET']
        port = settings['MYSQL_PORT']
        #数据库连接
        self.connect=pymysql.connect(host=host,user=user,passwd=psd,db=db,port=port, charset=c,use_unicode=True)
        #数据库游标
        self.cursor = self.connect.cursor();
        #执行一个测试语句，如果测试成功打印（未写）
        #print("mysql connect succes")  # 测试语句，这在程序执行时非常有效的理解程序是否执行到这一步

    def process_item(self, item, spider):

        #调用操作sql语句
        try:
            # data = dict(item)  # 将item变成字典形式
            # keys = ','.join(data.keys())  # 将字典的键值做成“，”隔开的字符串
            # values = ','.join(['%s'] * len(data))  # 根据data字典的长度建立对应长度数的“%s”
            # sql = 'insert into gup(%s) values %s' % (keys, tuple(data.values()))
            # print data.values()
            # print sql
            # self.cursor.execute(sql)  # 执行sql语句
            # self.connect.commit()  # 提交

            # 查重处理
            self.cursor.execute(
                """select * from gup where gpcode = %s""",
                "123")
            # 是否有重复数据
            repetition = self.cursor.fetchone()
            # 重复
            if repetition:
                pass
            else:

                # 插入数据
                # sql = """insert into gup(gpcode,kaipanjia) VALUES(%s,%s)"""  # sql语句，%s是占位符（%s是唯一的，不论什么数据类型都使用%s）用来防止sql注入
                # print item["gpcode"],item["kaipanjia"]
                # params = (item['gpcode'],'测试',)  # 参数
                # #params = ("1.1","2.2")  # 参数
                # print  params, u'提交',
                #print self.cursor.execute(sql, params)
                # 字典打印出16进制，如果现实中文，对dict 进行json转换，再打印
                str1 = json.dumps(dict(item), ensure_ascii=False) + "\n"

                # res = str(str1, encoding="utf-8")
                # list1 = json.loads(res)
                # print list1
                data = dict(item)  # 将item变成字典形式
                keys = ','.join(data.keys())  # 将字典的键值做成“，”隔开的字符串
                values = ','.join(['%s'] * len(data))  # 根据data字典的长度建立对应长度数的“%s”
                sql = 'insert into gup(%s) values %s' % (keys, tuple(data.values()))
               # print unicode(item['gocode'],encoding="utf-8")
                print self.cursor.execute(sql)
                # 提交sql语句
                self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            #logging(error)
            self.connect.rollback()
        self.connect.close()

        return item