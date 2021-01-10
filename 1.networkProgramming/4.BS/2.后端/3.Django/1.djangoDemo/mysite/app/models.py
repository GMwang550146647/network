from django.db import models

# Create your models here.
"""
1.创建表结构：
    1.1.ORM无法操作到数据库级别的命令，只能操作到数据表，所以第一步需要在数据库中创建表空间
        create database 数据库名称 default charset=utf8; # 防止编码问题，指定为 utf8
        create database mysite default charset=utf8;
    1.2.配置settings文件
        DATABASES = { 
            'default': 
            { 
                'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
                'NAME': 'runoob', # 数据库名称
                'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1 
                'PORT': 3306, # 端口 
                'USER': 'root',  # 数据库用户名
                'PASSWORD': '123456', # 数据库密码
            }  
        }
    1.3.settings同级目录下设置
        # 告诉 Django 使用 pymysql 模块连接 mysql 数据库：
        import pymysql
        pymysql.version_info = (1, 4, 13, "final", 0)
        pymysql.install_as_MySQLdb()
    1.4.定义模型
        1.表定义
            class Test(models.Model):
                name = models.CharField(max_length=20)
        2.创建表
            # python manage.py migrate   # 创建表结构
            # python manage.py makemigrations app  # 让 Django 知道我们在我们的模型有一些变更
            # python manage.py migrate app   # 创建表结构
        3.数据操作
        
"""


# 1.4.1.表定义
class UserInfo(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    hobby = models.CharField(max_length=30,default='nothing')
    normal = models.CharField(max_length=30,default='No')


# 1.4.2.数据库基本操作
def sql_api_template():
    # 1.insert
    test1 = UserInfo(id=100,username='gmwang', password='gmwang')
    test1.save()

    # 2.Select
    user_table = UserInfo.objects.all()  #->选全部
    seleted_rows = UserInfo.objects.filter(id=1)  #->where
    # seleted_row=UserInfo.objects.get(id=1) #获取一个
    for rowi in user_table:
        print(f"id:{rowi.id};\tusername:{rowi.username};\tpassword:{rowi.password}")

    # 3.update
    test2 = UserInfo.objects.get(id=2)
    test2.username = 'gmwang1'
    test2.save()

    # 4.delete
    test4 = UserInfo.objects.get(id=100)
    test4.delete()

def user_add(username,password,hobby,normal):
    new_user = UserInfo(username=username, password=password,hobby=hobby,normal=normal)
    new_user.save()

def user_login(username,password):
    users = UserInfo.objects.filter(username=username,password=password)
    return True if users else False

def get_users(*args,**kwargs):
    user_table = UserInfo.objects.all()
    return user_table

def edit_user(id,**kwargs):
    UserInfo.objects.filter(id=id).update(**kwargs)
    updated_user=UserInfo.object.filter(id=id)
    return updated_user[0]

def delete_user(id):
    UserInfo.objects.filter(id=id).delete()