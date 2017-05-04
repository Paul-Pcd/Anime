# -*- coding: utf-8 -*-

from multiprocessing import Pool
import json
import pymongo
import requests
import urllib
from bs4 import BeautifulSoup

client = pymongo.MongoClient('localhost', 27017)
bilibili = client['bilibili']
channels = bilibili['channels']
urls = bilibili['urls']
bangumi = bilibili['bangumi']
episodes = bilibili['episodes']


month = [0, 1, 4, 7, 10]

headers = {
    'Connection': 'keep-alive',
}


def get_urls_from(channel):
    url = channel['url']
    year = channel['year']
    month = channel['month']
    for page in ['1', '2', '3', '4']:
        wb_data = requests.get(url%(page), headers=headers)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        bangumi = json.loads(soup.select('p')[0].text)['result']['list']
        if len(bangumi) != 0:
            for item in bangumi:
                urls.insert_one({
                    'title': item['title'],
                    'year': year,
                    'month': month,
                    'id': item['url'].split('/')[-1],
                })


def get_bangumi_from(bangumi_url):
    try:
        id = bangumi_url['id']
        year = bangumi_url['year']
        month = bangumi_url['month']
        url = 'http://bangumi.bilibili.com/jsonp/seasoninfo/%s.ver?callback=seasonListCallback&jsonp=jsonp&_=1492439645551'
        wb_data = requests.get(url%(id), headers)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        data = soup.select('p')[0].text
        data = json.loads(data.strip('seasonListCallback(').strip(');'))['result']
        bangumi.insert_one({
            'title': data.get('bangumi_title'),
            'id': id,
            'actor': [(i['actor'], i['role']) for i in data['actor']],
            'play_count': data.get('play_count'),
            'favorites': data.get('favorites'),
            'evaluate': data.get('evaluate'),
            'danmaku_count': data.get('danmaku_count'),
            'year': year,
            'month': month,
            'cover': data.get('cover'),
            'tags': [i['tag_name'] for i in data.get('tags')],
        })

        # for i in data['episodes']:
        #     episodes.insert_one({
        #         'title': data.get('bangumi_title'),
        #         'id': id,
        #         'year': year,
        #         'month': month,
        #         'index': i.get('index'),
        #         'index_title': i.get('index_title'),
        #         'coins': i.get('coins'),
        #         'webplay_url': i.get('webplay_url'),
        #     })
    except Exception as e:
        print '{}\t{}'.format(id, e)


# 2581	Unterminated string starting at: line 1 column 1111 (char 1110)
# 1111	Expecting ',' delimiter: line 1 column 173 (char 172)
# 5132	'result'
# 3145	Expecting ',' delimiter: line 1 column 5458 (char 5457)
# 5795	Expecting ',' delimiter: line 1 column 5865 (char 5864)
# 4762	Expecting ',' delimiter: line 1 column 5807 (char 5806)


def get_avid(webplay_url):
    id = webplay_url.split('#')[-1]
    # http://bangumi.bilibili.com/web_api/episode/40814.json
    url = 'http://bangumi.bilibili.com/web_api/episode/{}.json'.format(id)
    wb_data = requests.get(url)
    data = json.loads(wb_data.text)
    av_id = data['result']['currentEpisode']['avId']
    return av_id


def get_details(av_id):
    # http://api.bilibili.com/archive_stat/stat?aid=170001
    url = 'http://api.bilibili.com/archive_stat/stat?aid={}'.format(av_id)
    wb_data = requests.get(url)
    data = json.loads(wb_data.text)['data']
    return {
        'coin': data['coin'],
        'view': data['view'],
    }


def fix_errors(li):
    pool = Pool()
    error_list = urls.find({
        'id': {'$in': li}
    })
    pool.map(get_bangumi_from, (i for i in error_list))

if __name__ == '__main__':
    pool = Pool()

    # pool.map(get_urls_from, (i for i in channels.find()))
    # print urls.find().count()

    pool.map(get_bangumi_from, (i for i in urls.find()))
    print bangumi.find().count()
    print episodes.find().count()





