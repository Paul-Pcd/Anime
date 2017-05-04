# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from mongoengine import *

connect('Bilibili', host='127.0.0.1', port=27017)


# 所有字段都要一一对应
class Bangumi(Document):
    _id = StringField()
    title = StringField()
    coins = StringField()
    tags = ListField(StringField())
    danmaku_count = IntField()
    favorites = IntField()
    year = IntField()
    month = IntField()
    actor = ListField(ListField(StringField()))
    evaluates = StringField()
    play_count = IntField()
    season_title = StringField()
    cover = URLField()

    meta = {'collection': 'Bangumi'}

    def bangumi_id(value):
        return value._id


class Episode(Document):
    _id = StringField()
    bangumi_id = StringField()
    cover = URLField()
    title = StringField()
    index = IntField()
    index_title = StringField()
    coins = IntField()
    year = IntField()
    month = IntField()
    webplay_url = URLField()
    cid = IntField()

    meta = {'collection': 'Episode'}

    def episode_id(value):
        return value._id