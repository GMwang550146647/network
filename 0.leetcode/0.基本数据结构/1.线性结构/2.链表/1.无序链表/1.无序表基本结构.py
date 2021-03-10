class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
class UnorderedList:
    def __init__(self):
        self.head=None
    #1.在最前面添加
    def add(self,value):
        tempt=Node(value)
        tempt.next=self.head
        self.head=tempt
        return True
    #2.判断是否空
    def isEmpty(self):
        return self.head == None
    #3.删除某个值
    def remove(self,item):
        if self.head==None:
            print("NO Found")
            return False
        elif self.head.value==item:
            if self.head.next!=None:
                self.head=self.head.next
            else:
                self.head=None
            print("Modified,%d deleted" % item)
            return True
        else:
            pre=self.head
            current=pre.next
            while(current!=None):
                if current.value==item:
                    pre.next=current.next
                    current=pre.next
                    print("Modified,%d deleted" % item)
                    return True
                else:
                    current=current.next
                    pre=pre.next
        return False
    #4.搜索某个值
    def search(self,item):
        tempt=self.head
        found=False
        while tempt!=None:
            if tempt.value==item:
                found=True
                break
            else:
                tempt=tempt.next
        return found
    #5.返回list的大小
    def size(self):
        tempt=self.head
        count=0
        while tempt!=None:
            count+=1
            tempt=tempt.next
        return count
    #6.在后面添加
    def append(self,item):
        current=self.head
        if self.head==None:
            self.head=Node(item)
        while(current.next!=None):
            current=current.next
        current.next=Node(item)
        return True
    #7.获取第i个
    def __getitem__(self,ith):
        return self.index(ith)
    def index(self,ith):
        size=self.size()
        if ith>=size:
            print("IndexError:arr.size=",size,",but index=",ith)
            return False
        elif ith ==-1:
            ith=size-1
        current=self.head
        for i in range(ith):
            current=current.next
        return current.value
    #8.在index处插入item
    def insert(self,ith,item):
        size=self.size()
        #最后一个，用append
        if ith>size:
            print("IndexError:arr.size=", size, ",but index=", ith)
            return False
        if ith==size:
            self.append(item)
        #首个用add
        elif ith==0:
            self.add(item)
        else:
            current = self.head
            for i in range(ith-1):  # 提取出arr[ith-1]那个
                current = current.next
            tempt=current.next
            current.next=Node(item)
            current.next.next=tempt
            return True

    #9.弹出index处的元素并返回，-1代表最后一个
    def pop(self,ith=-1):
        size=self.size()
        ith=size-1 if ith==-1 else ith
        #超出范围，和列表空的情况
        if ith>=size:
            print("IndexError:arr.size=", size, ",but index=", ith)
            return False
        if ith==0:
            val=self.head.value
            self.head=self.head.next
            return val
        current=self.head
        for i in range(ith-1):      #提取出arr[ith-1]那个
            current=current.next
        val=current.next.value
        current.next=current.next.next
        return val
    def __str__(self):
        current=self.head
        arr=[]
        while(current!=None):
            arr.append(current.value)
            current=current.next
        return str(arr)

'''1.测试add'''
arr=UnorderedList()
for i in range(10):
    arr.add(i)
print(arr)
print("~~~~~~~~~~~~~~~~~~~")
'''2.测试remove'''
arr.remove(7)
print(arr)
print("~~~~~~~~~~~~~~~~~~~")
'''3.测试search'''
print(arr.search(4))
print(arr)
print("~~~~~~~~~~~~~~~~~~~")
'''4.测试size'''
print(arr.size())
print(arr)
print("~~~~~~~~~~~~~~~~~~~")
'''5.测试index'''
print(arr[-1])
print(arr)
print("~~~~~~~~~~~~~~~~~~~")
'''6.测试append'''
arr.append(1989189)
print(arr)
print("~~~~~~~~~~~~~~~~~~~")
'''7.测试insert'''
arr.insert(4,3948834028)
print("~~~~~~~~~~~~~~~~~~~")
'''8.测试isEmpty'''
print(arr.isEmpty())
print("~~~~~~~~~~~~~~~~~~~")
'''9.测试pop'''
print(arr.pop())
print(arr)
print("~~~~~~~~~~~~~~~~~~~")