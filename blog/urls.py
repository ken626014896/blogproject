

from django.contrib import admin
from django.urls import path,re_path

from blog  import  views

urlpatterns=[
    path('',views.index,name="index"),
    re_path(r'^post/(?P<pk>[0-9]+)/$',views.detail,name="detail"),
    re_path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    re_path(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category')


]