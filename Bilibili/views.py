# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from pure_pagination import Paginator, PageNotAnInteger
from mongoengine import Q
from collections import Counter

import json

from Bilibili.models import Bangumi, Episode


def get_episode_coins(bangumi_id):
    all_episodes = Episode.objects.filter(bangumi_id=bangumi_id).order_by('index')
    data = [{"name": "第{}话".format(episode['index']), "y": episode['coins']} for episode in
            all_episodes]
    return data


class IndexChartDataView(View):

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


class EpisodesCoinCount(View):

    def get(self, request):
        data = get_episode_coins(request.GET.get("bangumi_id"))
        return HttpResponse(json.dumps(data), content_type='application/json')


class BangumiListView(View):

    def get(self, request):
        # 搜索
        keywords = request.GET.get('keywords', '')
        all_bangumi = Bangumi.objects.filter(
            Q(title__icontains=keywords) |
            Q(evaluates__icontains=keywords)
        ).order_by('-year')

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_bangumi, 15, request=request)     # 每页显示个数必须指定
        all_bangumi = p.page(page)

        return render(request, 'bangumi-list.html', {
            'Bangumis': all_bangumi,
        })


class BangumiDetailView(View):

    def get(self, request, bangumi_id):
        bangumi = Bangumi.objects.filter(_id=bangumi_id)[0]
        all_episodes = Episode.objects.filter(bangumi_id=bangumi_id).order_by('index')
        return render(request, 'bangumi-detail.html', {
            "Bangumi": bangumi,
            "Episodes": all_episodes,
        })


class IndexView(View):
    def get(self, request):

        bangumi_number = Bangumi.objects.count()
        episodes_number = Episode.objects.count()

        return render_to_response('index.html', {
            'bangumi_number': bangumi_number,
            'episodes_number': episodes_number,
            })
