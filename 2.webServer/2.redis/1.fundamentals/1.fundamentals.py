
"""
查看帮助
    命令 + --help
        例如： redis-server --help
命令：
redis-server    #redis服务端启动
    配置文件在 /usr/local/etc/redis.conf
redis-cli       #redis客户端启动
    -h ip地址
    -p 端口
    -s 套接字
    -a 密码
    -n 指定的redis库（默认有16个）
    redis命令不区分大小写
redis-benchmark #性能测试
    例如  redis-benchmark -q
redis-check-aof #检查修复aof文件
redis-check-rdb #检查修复rdb文件
redis-sentinel  #redis集群
redis-trib.rb   #集群管理
"""
"""
连接服务之后的命令
    1.测试连接  ping
    2.查看信息 info
    3.打印内容 echo
    4.退出 quit
    5.设置 set [key] [value]
    6.获取 get [key]
    7.删除 del [key]
    8.选择库  select 0-16 (默认0）
    9.判存在  exists [key]
    10.设有时限的变量  expire [key] [n seconds]  （毫秒pexpire）
    11.查看剩余存活时间 TTL [key]                （毫秒pttl）
    12.key的模糊匹配 TTL [key *]
    13.查看key[模糊匹配] keys pattern   -> example: keys gmwang* (开头为gmwang的所有key)
    14.key的数据库转移  move [key] [db]
    15.随机获取一个key randomkey
    16.重命名 key  rename [key] [new key] （如果存在则rename,不存在则报错）
    17.查看类型 type [key]  若无则返回none
数据结构相关
    string
    list
    hash
    set 
    
    详见 https://www.runoob.com/redis/redis-server.html
主从
    从服务器上面配置
        slaveof [ip]  [port]
        如果有密码
            masterauth [password]
        命令行设置
            config set masterauth [password]
"""