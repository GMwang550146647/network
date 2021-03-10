'''
二叉堆：根节点最小，叶节点最大（或者相反）
'''
from pythonds.trees.binheap import BinHeap
bh=BinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())