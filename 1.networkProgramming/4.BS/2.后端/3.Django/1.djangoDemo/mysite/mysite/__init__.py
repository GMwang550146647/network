# 在与 settings.py 同级目录下的 __init__.py 中引入模块和进行配置
# 告诉 Django 使用 pymysql 模块连接 mysql 数据库：
import pymysql

pymysql.install_as_MySQLdb()
