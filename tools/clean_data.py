# -*- coding: utf-8 -*-

import pymongo

Client = pymongo.MongoClient("localhost", 27017)
Bilibili = Client["Bilibili"]
Bangumi = Bilibili["Bangumi"]
Episode = Bilibili["Episode"]

# for i in Episode.find():
#     if i["index"]:
#         try:
#             index = float(i["index"])
#             Episode.update({"_id": i["_id"]}, {"$set": {"index": index}})
#         except Exception as e:
#             print e
#     if i["coins"]:
#         coins = int(i["coins"])
#         Bilibili.update({"_id": i["_id"]}, {"$set": {"coins": coins}})

for i in Bangumi.find():
    # if i["favorites"]:
    #     try:
    #         favorites = int(i["favorites"])
    #         Bangumi.update({"_id": i["_id"]}, {"$set": {"favorites": favorites}})
    #     except Exception as e:
    #         print e
    # if i["danmaku_count"]:
    #     try:
    #         danmaku_count = int(i["danmaku_count"])
    #         Bangumi.update({"_id": i["_id"]}, {"$set": {"danmaku_count": danmaku_count}})
    #     except Exception as e:
    #         print e
    if i["play_count"]:
        try:
            play_count = int(i["play_count"])
            Bangumi.update({"_id": i["_id"]}, {"$set": {"play_count": play_count}})
        except Exception as e:
            print(e)
