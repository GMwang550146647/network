"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from app import views

urlpatterns = [
    # 1.简单路由，需要完全匹配
    path('admin/', admin.site.urls),
    path('signup/', views.signup),
    path('database/', views.database),
    path('request/', views.request),
    path('template_system/', views.template_system),
    path('template_inherit1/', views.template_inherit1),
    path('template_inherit2/', views.template_inherit2),
    path('user_management/', views.user_management),

    # 2.正则路由，正则匹配
    re_path('^login/', views.login, name='lg'),  # 只要这个正则match 就会执行这里 #->别名 用于反向解释！就是把页面中的 {% url 'lg' [args] %} 解析为  'login/'
    re_path('^login1/', views.Login.as_view()),  # 只要这个正则match 就会执行这里
    # url('^login/.*', views.login),  # 只要这个正则match 就会执行这里
    url('^delete_user/(\d+)/', views.delete_user,name='delete'),
    url('^edit_user/', views.edit_user,name='edit'),

    # 3.无名路由 :传入的参数要按顺序，index1有三个参数 ： request, m,n
    url(r'^index/(\d+)/(\d+)/', views.IndexView.as_view()),

    # 4.有名路由 :传入的参数可以不按顺序，相当于**dict,但是名字一定要对应上
    url(r'^index/(?P<year>\d+)/(?P<month>\d+)', views.index2),

    # 5.分发路由:只要是demo1开头的都往这里走
    url(r'^demo1/', include('demo1.urls')),
    # url(r'^books/', include('books.urls'))
]
