"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31 ,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
import time


num=-990090909
'''1.我的答案'''
def myFun(num):
    #32位最大是4294967296
    arr=[]
    #第一步：判断正负
    flag=1 if num>=0 else -1
    num=num if num>=0 else -num
    #第二步：去掉末尾的0：
    while(num%10==0):
        num=num/10
    #第二步：把每个数字拆分到列表中：
    for i in range(15):
        tempt_num=num%10
        arr.append(tempt_num)
        num=num//10
        if 1<=num<10:
            arr.append(num)
            break
    #第三步：从arr中翻转数字
    result=0
    length=len(arr)
    for i in range(length):
        result+=arr[i]*10**(length-1-i)
    #第四步：符号判断
    return result*flag
#计时
start = time.process_time()
result=myFun(num)
elapsed = (time.process_time() - start)
print("Time used:",elapsed)
print('result:',result)


'''2.参考答案'''
'''
原理：result=result*10+num%10 ,连数组都省了
'''
def SA(num):
    sign=1 if num>=0 else -1
    num=num if num>=0 else -num
    result=0
    while(num>0):
        result=result*10+num%10
        num=num//10
    return sign*result if result<=2**32 else 0
#计时器
start = time.process_time()
result=SA(num)
elapsed = (time.process_time() - start)
print("Time used:",elapsed)
print('result:',result)
