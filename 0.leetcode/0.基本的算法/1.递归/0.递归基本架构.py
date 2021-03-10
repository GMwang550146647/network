import sys
'''1.查看递归层数'''
print('default:',sys.getrecursionlimit())
'''2.设定递归层数'''
sys.setrecursionlimit(3000)
print('after modified:',sys.getrecursionlimit())
