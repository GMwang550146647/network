"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import time

'''1.我的答案'''
nums = [2, 7, 11, 15,3,5,6]
def myFun(nums,target):
    answer=[]
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                answer.append((i,j))
                return answer
    return answer

#计时器
start = time.process_time()
result=myFun(nums,9)
elapsed = (time.process_time() - start)
print("Time used:",elapsed)
print('result:',result)


'''2.参考答案'''
'''
原理：为了防止重复计算，用字典把target-num的结果存储起来，如果发现下一个数刚好在结果集合里面，
就把其index拿出来。例如一开始9-2=7，7不在字典中把2记录在字典中（看后面有没有差是2的），继续下一个，
当到7时发现9-7=2，所以就把2对应的index：0拿出来，最后和7对应的index：1一起返回
'''
def SA(nums,target):
    d={}
    for i,num in enumerate(nums):
        if target-num in d:
            return [d[target-num],i]
        d[num]=i

#计时器
start = time.process_time()
result=SA(nums,9)
elapsed = (time.process_time() - start)
print("Time used:",elapsed)
print('result:',result)