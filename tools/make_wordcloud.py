# -*- coding: utf-8 -*-

import pymongo
from collections import Counter
import jieba
import random
import codecs
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


Client = pymongo.MongoClient("localhost", 27017)
Bilibili = Client["Bilibili"]
Episode = Bilibili["Episode"]
Bangumi = Bilibili["Bangumi"]
Comment = Bilibili["Comment"]


def jieba_cut(line):
    return jieba.cut(line)


def normal_cut(line):
    return line.split(",")


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


def count_word(id_list):
    word_counter = []
    for bangumi_id in id_list:
        for i in Comment.find({"bangumi_id": bangumi_id}):
            comment = i["comment"].replace("/", ",")
            for word in normal_cut(comment):
                word_counter.append(word) if word != "," else None
    # word_counter = Counter(word_counter).most_common()
    return Counter(word_counter)


# 生成评论文件
def create_text_file(bangumi_id):
    with codecs.open("E:/Projects/Bangumi/{}.txt".format(bangumi_id), "w", encoding="utf-8") as f:
        for i in Comment.find({"bangumi_id": bangumi_id}):
            comment = i["comment"].replace("/", ",")
            f.write(comment+"\r\n")


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


def create_cloud(id_list):
    font = "E:/Projects/Bangumi/DroidSansFallback.ttf"
    # mask = plt.imread("E:/Projects/Bangumi/Python.jpg")
    # coloring = np.array(Image.open("E:/Projects/Bangumi/Python.jpg"))
    # image_colors = ImageColorGenerator(coloring)
    #
    # wordcloud = WordCloud(mask=mask, font_path=font, margin=10, random_state=1)
    # wordcloud = wordcloud.generate_from_frequencies(count_word(bangumi_id))
    #
    # default_colors = wordcloud.recolor(color_func=image_colors)
    # plt.imshow(default_colors)
    #
    # wordcloud.to_file("E:/Projects/Bangumi/{}.jpg".format(bangumi_id))
    mask = np.array((Image.open("wordclouds/Python.jpg")))
    wordcloud = WordCloud(background_color="white", mask=mask, font_path=font, margin=10, random_state=1, max_font_size=100)
    wordcloud = wordcloud.generate_from_frequencies(count_word(id_list))
    plt.imshow(wordcloud)
    wordcloud.to_file("wordclouds/{}.jpg".format('test'))

create_cloud(["3461", "3450", "5800", "5550", "5997", "5017", "3462", "3494", "5747", "1586"])
