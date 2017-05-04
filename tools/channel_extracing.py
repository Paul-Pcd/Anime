# -*- coding: utf-8 -*-

import pymongo
import requests
from bs4 import BeautifulSoup

January, April, july, October = 1, 2, 3, 4
client = pymongo.MongoClient('localhost', 27017)
bilibili = client['bilibili']
channels = bilibili['channels']

months = [0, 1, 4, 7, 10]


# 获取从1970年1月至2017年1月的番剧索引页
def get_channel_urls():
    for year in range(1970, 2017):
        for month in range(1, 5):
            channel = 'http://bangumi.bilibili.com/web_api/season/index_global?page=%s&page_size=20&version=0&is_finish=0&start_year={}&tag_id=&index_type=1&index_sort=0&quarter={}'.format(year, month)
            channels.insert_one({
                'url': channel,
                'year': year,
                'month': months[month],
            })
    channels.insert_one({
        'url': 'http://bangumi.bilibili.com/web_api/season/index_global?page=%s&page_size=20&version=0&is_finish=0&start_year=2017&tag_id=&index_type=1&index_sort=0&quarter=1',
        'year': 2017,
        'month': 1,
    })


get_channel_urls()