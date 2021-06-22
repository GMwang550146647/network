'''
10.高阶函数：接收函数作为参数，或者将函数作为返回值的函数
'''
'''1.函数作为参数存入'''
l=[1,2,3,4,5,6,7,8,9,10]

def isOdd(num):
    if num%2==0:
        return True
    else:
        return False
def filter1(l,filterFunc):
    li=[]
    for item in l:
        if filterFunc(item):
            li.append(item)
    return li

print(filter1(l,filterFunc=isOdd))


'''2.函数作为返回值返回（闭包）'''
'''
使用条件：
1.函数嵌套
2.内部函数作为函数返回
3.内部函数必须要使用到外部函数的变量
'''
def fn():
    '''在fn内部定义，并把不是全局函数，所以这个函数能访问到fn()内部的变量'''
    nums=[]
    def average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return average
averageAdd=fn()
print(averageAdd(10))
print(averageAdd(20))
print(averageAdd(30))
print(averageAdd(40))
print(averageAdd(50))
print(averageAdd(60))

