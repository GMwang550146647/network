'''
ADT Map
'''
class HashTable:
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size
        self.data=[None]*self.size
    def hashfunction(self,key):
        return key%self.size
    def rehash(self,oldhash):
        return (oldhash+1)%self.size
    def put(self,key,data):

        hashvalue=self.hashfunction(key)
        #当该hashvalue还是空的时候
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        #hashvalue非空
        else:
            #虽然非空，但是和要填的一样（说明是修改）
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data
            #非空而且已有占位,rehash,直至找到位置
            else:
                if not None in self.slots:
                    print("error:hashtable full,can not add")
                    return
                nextslot=self.rehash(hashvalue)
                #直至找到空位或者相同的key的时候停止
                while self.slots[nextslot]!=None and self.slots[nextslot]!=key:
                    nextslot=self.rehash(nextslot)
                if self.slots[nextslot]==key:
                    self.data[nextslot]=data
                else:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
    def get(self,key):
        startslot=self.hashfunction(key)
        data=None
        pos=startslot
        stop=False
        found=False
        while self.slots[pos]!=None and not stop and not found:
            if self.slots[pos]==key:
                found=True
                data=self.data[pos]
            else:
                pos=self.rehash(pos)
                if pos==startslot:
                    stop=True
        return data
ht=HashTable()
for i in range(10):
    ht.put(i,i*10)
for i in range(1,15,2):
    print(i,":",ht.get(i))

ht.put(11,110)
print(11,":",ht.get(11))
#已满不能再增加了
ht.put(12,120)
print(12,":",ht.get(12))
