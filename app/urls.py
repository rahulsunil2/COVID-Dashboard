# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path

from app import views

urlpatterns = [

    path('containment_zones', views.containment_zones, name='containment_zones'),
    path('essentials_list', views.essential_items_list, name='essentials_list'),
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
]
