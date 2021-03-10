class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
class UnorderedList:
    def __init__(self):
        self.head=None
    #1.在最前面添加
    def add(self,item):
        current=self.head
        #1.如果列表为空
        if self.head==None:
            self.head=Node(item)
        #如果列表不为空，创建一个prev
        else:
            prev=self.head
            current=self.head.next
            while(current!=None and current.value<item):
                prev=current
                current=current.next
            tempt = prev.next
            prev.next = Node(item)
            prev.next.next = tempt
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
    #6.获取第i个
    def __getitem__(self,ith):
        return self.index(ith)
    def index(self,ith):
        size=self.size()
        if ith>=size:
            print("IndexError:arr.size=",size,",but index=",ith)
            return False
        current=self.head
        for i in range(ith):
            current=current.next
        return current.value

    #7.弹出index处的元素并返回，-1代表最后一个
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
'''8.测试isEmpty'''
print(arr.isEmpty())
print("~~~~~~~~~~~~~~~~~~~")
'''9.测试pop'''
print(arr.pop())
print(arr)
print("~~~~~~~~~~~~~~~~~~~")