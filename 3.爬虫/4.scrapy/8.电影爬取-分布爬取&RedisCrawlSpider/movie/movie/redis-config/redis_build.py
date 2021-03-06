'''
redis-server redis.conf
    # 关闭默认绑定 #bind 127.0.0.1
    # 关闭保护模式 #protected-mode no

关闭redis服务 ： redis-cli -p 6379 shutdown
'''
import subprocess
subprocess.check_call('redis-server redis.conf'.split())