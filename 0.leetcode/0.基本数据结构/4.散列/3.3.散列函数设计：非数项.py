'''
1.普通方法：把字母转换成数值再运算

'''
def hash(astring,tablesize):
    sum=0
    for pos in range(len(astring)):
        sum+=ord(astring[pos])
    return sum%tablesize

'''
2.强化方法：为了保证字母一样时，但是位置不一样的情况的区别，加上位置权重
'''
def hashR(astring,tablesize):
    sum=0
    for pos in range(len(astring)):
        sum+=ord(astring[pos])*(pos+1)
    return sum%tablesize