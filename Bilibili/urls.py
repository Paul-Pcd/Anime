# -*- coding: utf-8 -*-

from django.conf.urls import url
from Bilibili.views import BangumiListView, BangumiDetailView, EpisodesCoinCount

urlpatterns = [
    # 此时通过http://127.0.0.1:8000/bangumi/list/访问
    url(r'^list/$', BangumiListView.as_view(), name='bangumi_list'),
    url(r'^coin_count/$', EpisodesCoinCount.as_view(), name='coin_count'),
    url(r'^detail/(?P<bangumi_id>\d+)/$', BangumiDetailView.as_view(), name='bangumi_detail'),
]
