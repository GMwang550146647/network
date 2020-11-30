"""
sql基本命令
1.进入数据库
    1.1.普通进入
        mysql
        查看当前用户
            select user();
    1.2.带用户进入
        mysql -u root
            设置密码
                set password = password("->CODE")
    1.3.带用户密码进入
        mysql -u root -p xxx
    1.4.连接远程服务器
        mysql -u USER_NAME -p PASSWORD -h 192.168.31.13
            例如 mysql -u gmwang -h 192.168.31.13
                mysql -u root -h 192.168.31.13

2.创建用户并设置权限 (注意：设置完一定要FLUSH PRIVILEGES;）
    2.1.创建用户
        create user 'USER_NAME'@'192.168.31.%' identified by 'PASSWORD'  -> 192.168.31.% 这个网段的人都可以访问
        例如  create user 'gmwang'@'192.168.31.%' identified by 'gmwang';
    2.2.权限控制
        grant 权限类型 on 库[.表名]  to 'USER_NAME'@'192.168.31.%';
            例如  grant all on employees.*  to 'gmwang'@'192.168.31.%';
        grant all
        grant select
        grant select, insert
    2.3.创建并赋权
        grant all on *.* to 'USER_NAME'@'192.168.31.%' identified by 'PASSWORD';
    2.4.查看某用户权限
        show grants for 'USER_NAME'@'192.168.31.%';
            例如  grant all on employees.*  to 'gmwang'@'192.168.31.%';
    2.5.删除用户
        drop user 'USER_NAME'@'192.168.31.%';
"""
"""
数据库操作
1.操作数据库(DCL) CONTROL
    查看所有数据库 show databases;
    创建数据库    create database 数据库名字;
    切换到某数据库 use 数据库名字;
    查看某数据库的表 show tables;
    删除数据库     drop database 数据库名字;

2.表操作(DDL)   DEFINE
    创建表格    create table 表名(字段1 type1, 字段2 type2...)
    查看表结构   desc 表名; -> describe 表名;
    删除表      drop table 表名;

3.表内容操作(DML) MANAGEMENT
    插入(增）  insert into 表名 values (xxx,xxx,xxx...)
    删除(删)  delete from student where columni= 'xxx';
    修改(改)  update student set columni=xxx,columnj=xxx where columnj='xxx';
    查询(查)  select * from 表名;
"""