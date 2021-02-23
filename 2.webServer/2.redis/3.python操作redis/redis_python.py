import redis
"""
1.连接单个服务器
"""
try:
    r = redis.StrictRedis(
        host='127.0.0.1',
        port='6379',
    )
    r.set('gmwang','feifei')
    print(r.get("gmwang"))
except Exception as e:
    print("Single Connection Error: {}".format(str(e)))

"""
2.连接集群
pip install redis-py-cluster
"""
from rediscluster import RedisCluster
try:
    startup_nodes = [
        {'host': '127.0.0.1', 'port': 6371},
        {'host': '127.0.0.1', 'port': 6372},
        {'host': '127.0.0.1', 'port': 6373},
    ]
    r=RedisCluster(
        startup_nodes=startup_nodes,
        decode_responses=True,
        # password=None
    )
    r.set('gmwang','feifei')
    print(r.get('gmwang'))
except Exception as e:
    print("Cluster Connection Error:{}".format(str(e)))
