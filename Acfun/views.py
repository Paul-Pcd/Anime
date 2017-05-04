# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from pure_pagination import Paginator, PageNotAnInteger
from mongoengine import Q
from collections import Counter

import json

class NewsListView(View):
    pass

