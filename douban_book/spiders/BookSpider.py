import scrapy
from douban_book.items import TjItem
import json


class BookSpider(scrapy.Spider):
    name = 's_tencent'
    allowed_domains = ['careers.tencent.com']
    # 开始链接
    start_urls = []
    # 循环添加api链接
    for page in range(1, 62):
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?keyword=python&pageIndex=%s&pageSize=10' % page
        start_urls.append(url)

    def parse(self, response):
        content = response.body.decode('utf-8')  # 将response响应的数据存到content变量中
        data = json.loads(content)  # 格式化为json数据
        job_list = data['Data']['Posts']
        for job in job_list:
            item = TjItem()  # 创建item实例
            # 将数据存入item
            item['recruitPostId'] = job['RecruitPostId']
            item['recruitPostName'] = job['RecruitPostName']
            item['countryName'] = job['CountryName']
            item['locationName'] = job['LocationName']
            item['GName'] = job['BGName']
            item['productName'] = job['ProductName']
            item['categoryName'] = job['CategoryName']
            item['responsibility'] = job['Responsibility']
            item['lastUpdateTime'] = job['LastUpdateTime']
            item['postURL'] = job['PostURL']
            # 创建一个字典info
            info = {
                "RecruitPostId": item['recruitPostId'],
                "RecruitPostName": item['recruitPostName'],
                "CountryName": item['countryName'],
                "LocationName": item['locationName'],
                "BGName": item['GName'],
                "ProductName": item['productName'],
                "CategoryName": item['categoryName'],
                "Responsibility": item['responsibility'],
                "LastUpdateTime": item['lastUpdateTime'],
                "PostURL": item['postURL'],
            }
            # 传给pipeline
            yield item

            # 将数据写入txt文本文件
            with open('job.txt', 'a', encoding='utf-8') as fp:
                fp.write(str(info) + '\n')
