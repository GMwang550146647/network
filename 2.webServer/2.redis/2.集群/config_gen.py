import os
"""
1.config 生成
"""
def config_gen():
    dir='config'
    os.makedirs(dir,exist_ok=True)
    str="bind 127.0.0.1\n" \
        "port {}\n" \
        "daemonize yes\n" \
        "pidfile {}.pid\n" \
        "logfile {}.log\n" \
        "cluster-enabled yes\n" \
        "cluster-config-file node-{}.conf\n" \
        "cluster-node-timeout 10000\n"
    for i in range(7):
        num=6371+i
        stri=str.format(num,num,num,num)
        with open(os.path.join(dir,"config{}.conf".format(num)),'w') as f:
            f.write(stri)
"""
[help: redis-cli --cluster help]
2.安装ruby
    brew install ruby
    sudo gem install redis

3.建立服务
    redis-server xxx.config
    创建create :   redis-cli --cluster create --cluster-replicas 1 127.0.0.1:6371 127.0.0.1:6372 127.0.0.1:6373 127.0.0.1:6374 127.0.0.1:6375 127.0.0.1:6376
    检查check  :   redis-cli --cluster check [host:port]
    信息info   :   redis-cli --cluster info [host:port]
    修复fix    :   redis-cli --cluster fix  [host:port]
    添加节点add-node: redis-cli --cluster add-node 127.0.0.1:6377 127.0.0.1:6371
    删除节点del-node :   redis-cli --cluster del [host:port]
4.连接集群
    redis-cli -c -p [port]  
    
"""

if __name__ == '__main__':
    config_gen()