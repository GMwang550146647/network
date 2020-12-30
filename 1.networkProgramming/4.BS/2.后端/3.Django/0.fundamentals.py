"""
1.MVC
    1.模型(M)         负责业务对象和数据库的关系映射(ORM)
    2.控制器(C)        接受用户的输入调用模型和视图完成用户的请求
    3.视图(V)         负责业务逻辑，并在适当时候调用Model和Template
2.MTV
    1.模型(Model)：   负责业务对象和数据库的关系映射(ORM)。
    2.模板(Template)：负责如何把页面展示给用户(html)。
    3.视图(View)：    负责业务逻辑，并在适当时候调用Model和Template。

3.Django
    1.主项目
        1.1.创建目录架构
            创建：django-admin startproject mysite

        1.2.具体目录架构
            mysite
            ├── mysite
            │   ├── __init__.py
            │   ├── asgi.py
            │   ├── settings.py       包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。
            │   ├── urls.py           负责把URL模式映射到应用程序
            │   └── wsgi.py           runserver命令就使用wsgiref模块做简单的web server，后面会看到renserver命令，所有与socket相关的内容都在这个文件里面了，目前不需要关注它。
            └── manage.py             Django项目里面的工具，通过它可以调用django shell和数据库，启动关闭项目与项目交互等，不管你将框架分了几个文件，必然有一个启动文件，其实他们本身就是一个文件。
    2.应用程序
        1.1.创建应用程序目录架构
            创建： python manage.py startapp app

        1.2.具体目录架构
            app
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── migrations
            │   └── __init__.py
            ├── models.py
            ├── tests.py
            └── views.py

    3.运行
        python manage.py runserver 127.0.0.1:8080  （默认8000端口）
"""
import django
