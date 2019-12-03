# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.item import Item
import json
from scrapy.exceptions import DropItem

class DoubanBookPipeline(object):
    def process_item(self, item, spider):
        return item





class MongoDBPipeline(object):

    # 读取MongoDB中的MONGO_DB_URI
    # 读取MongoDB中的MONGO_DB_NAME
    @classmethod
    def from_crawler(cls, crawler):
        cls.DB_URI = crawler.settings.get('MONGO_DB_URI')
        cls.DB_NAME = crawler.settings.get('MONGO_DB_NAME')
        return cls()

    def __init__(self):
        pass

    # 打开爬虫之前连接MongoDB
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URI, username='rw',password='ok')
        self.db = self.client[self.DB_NAME]

    # 关闭爬虫时关闭数据库
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]  # 设置MongoDB的表明为爬虫名
        post = dict(item) if isinstance(item, Item) else item  # 以dict形式存入数据库
        collection.insert_one(post)  # 插入数据
        return item  # 返回ite


# json格式
class JsonPipeline(object):

    # 初始化
    def __init__(self):
        self.f = open("TJ.json", "w")

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()
