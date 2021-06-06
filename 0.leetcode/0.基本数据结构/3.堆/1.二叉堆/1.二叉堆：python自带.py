'''
二叉堆：根节点最小，叶节点最大（或者相反）
'''
import heapq
from random import shuffle

lt = list(range(100))
lt1 = list(range(99))
shuffle(lt)
heapq.heappush(lt1, 99)
heapq.heapify(lt)
print(lt)
print(lt1)
for  i in range(100):
    print(heapq.heappop(lt1))