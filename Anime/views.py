# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.views.generic import View
from django.http import HttpResponse
from collections import Counter

import json

from Bilibili.models import Bangumi, Episode


class ChartDataView(View):

    def get_favorite_count(self):
        all_bangumis = Bangumi.objects.order_by("-favorites")[:8]
        data = [{"name": bangumi["title"], "y": bangumi["favorites"]} for bangumi in all_bangumis]
        return data

    def get_episode_coins(self):
        data = []
        all_bangumis = Bangumi.objects.order_by("-favorites")[:5]
        for bangumi in all_bangumis:
            bangumi_id = bangumi["_id"]
            bangumi_name = bangumi["title"]
            all_episodes = Episode.objects.filter(bangumi_id=bangumi_id).order_by('index')
            data.append({
                "name": bangumi_name,
                "data": [{"name": "第{}话".format(episode['index']), "y": episode['coins']}
                         for episode in all_episodes]
            })
        return data

    def get_tags_count(self):
        tags = []
        for bangumi in Bangumi.objects.all():
            for tag in bangumi["tags"]:
                tags.append(tag)
        data = [{"name": bangumi[0], "y": bangumi[1]} for bangumi in Counter(tags).most_common(8)]
        return data

    def get(self, request):
        key = request.GET.get("key")
        data = getattr(self, key)()
        return HttpResponse(json.dumps(data), content_type="application/json")


class IndexView(View):
    def get(self, request):
        return render_to_response(
            'index.html',
        )
