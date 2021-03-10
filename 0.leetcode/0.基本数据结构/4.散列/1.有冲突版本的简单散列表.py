#例如python的字典结构
'''
1.简单hash函数实现示例（有冲突版本）：
    前提：理想情况下，数据不变动，散列表足够大不出现冲突，称为完美散列函数
    问题：在数列【26，77，93，17，31，54】数列中查找是否存在某个数
    解决：利用hashfunc= num%11的方法把数放在十一个槽中
'''


class hashTable:
    def __init__(self,arr,volumn=11):
        self.hashTable=[-1 for i in range(11)]
        self.volumn=volumn
        self.initHashtable()
    '''1.1.存储算法'''
    def initHashtable(self):
        for num in arr:
            index=num%self.volumn
            self.hashTable[index]=num

    '''1.2.查找算法'''
    def findnum(self,num):
        if self.hashTable[num%self.volumn]==num:
            return True
        else:
            return False

arr=[26,77,93,17,31,54]
ht=hashTable(arr)
print(ht.findnum(93))
print(ht.findnum(94))
