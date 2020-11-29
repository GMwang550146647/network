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
    2.3.查看某用户权限
        show grants for 'USER_NAME'@'192.168.31.%';
            例如  grant all on employees.*  to 'gmwang'@'192.168.31.%';
"""