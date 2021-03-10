#例如python的字典结构
'''
1.解决冲突hash函数实现示例）：
    问题：在数列【26，77，93，17，31，54】数列中查找是否存在某个数
    解决：利用hashfunc= num%11的方法把数放在十一个槽中,每个槽都是一个数组
'''


class hashTable:
    def __init__(self,arr,volumn=11):
        self.hashTable=[[] for i in range(11)]
        self.volumn=volumn
        self.initHashtable()
        print(self.hashTable)
    '''1.1.存储算法'''
    def initHashtable(self):
        for num in arr:
            index=num%self.volumn
            self.hashTable[index].append(num)

    '''1.2.查找算法'''
    def findnum(self,num):
        index=num%self.volumn
        for i in range(len(self.hashTable[index])):
            if num==self.hashTable[index][i]:
                return True
        return False

arr=[26,77,93,17,31,54,44,55]
ht=hashTable(arr)
print(ht.findnum(93))
print(ht.findnum(94))
