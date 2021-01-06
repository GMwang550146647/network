from demo1 import views
from django.urls import path, re_path,include
from django.conf.urls import url

urlpatterns = [
    url(r'^index/',views.index),
    url(r'^$',views.home)
]