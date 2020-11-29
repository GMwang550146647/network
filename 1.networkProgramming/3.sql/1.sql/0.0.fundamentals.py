"""
数据库
    分类
        关系型db    相对慢
            例子： sqllite,db2,oracle,access,sql,MYSQL
        非关系型db  相对快
            例子： mongodb，redis，memcache
    例如：MySQL，Qracle，SQLite，Access，MS SQL Server
        mysql用于大型门户，例如搜狗，新浪，主要优势是开源代码
        oracle用于银行，铁路，飞机场。功能强大，软件费用高
        sql server微软，用于大中型企业，如联想，方正等...
数据库作用
    1.程序稳定性：任意一台服务器所在的机器崩溃了都不影响数据和另外的服务
    2.数据一致性：所有数据存在一起，所有操作的数据都是统一的，不会出现不一致
    3.并发：数据库支持并发，所有程序操作数据库都是通过网络，数据库支持并发网络操作，不需要自己写socket
    4.效率：通过数据库对数据进行增删改查，比我们自己处理文件效率高很多
安装
    安装并使用python接口           详情：https://dev.mysql.com/doc/connector-j/8.0/en/
        1.软件下载以及接口下载并安装：https://dev.mysql.com/doc/connector-python/en/connector-python-obtaining.html
        2.pip安装 Connector/Python： pip install mysql-connector-python
    安装并使用数据库                详情：https://dev.mysql.com/doc/refman/8.0/en/osx-installation.html
        1.

"""


if __name__ == '__main__':
    """
    一.cmd使用数据库
        1.cmd 开启数据库服务
            cd /Library/LaunchDaemons
            sudo launchctl load -F com.oracle.oss.mysql.mysqld.plist
        2.自定义配置数据库
            sudo launchctl load -w com.oracle.oss.mysql.mysqld.plist
        3.配置文件改别名
            vi ~/.bash_profile  
                加入以下两行
                  alias mysql=/usr/local/mysql/bin/mysql
                  alias mysqladmin=/usr/local/mysql/bin/mysqladmin
        4.具体的配置文件（可以自行更改）
            cat /Library/LaunchDaemons/com.oracle.oss.mysql.mysqld.plist
            
        5.登录数据库 
            mysql -u root -p
    """

    """
    二.使用数据库接口
    """
    from distutils.sysconfig import get_python_lib

    print(get_python_lib())  # Python v3.x

    """
    三.使用数据库接口
    """

    import mysql.connector
    # cnx = mysql.connector.connect(user='scott', password='password',
    #                               host='127.0.0.1',
    #                               database='employees')
    cnx = mysql.connector.connect(host='127.0.0.1',)
    cnx.close()

