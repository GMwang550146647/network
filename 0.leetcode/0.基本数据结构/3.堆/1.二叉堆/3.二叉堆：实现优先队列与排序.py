'''列表实现'''
class BinaryHeap():
    def __init__(self):
        self.heapList=[0] #第一位不用
        self.currentSize=0
    '''insert:为了保证完全二叉树，要放在列表最后，但是会破坏次序，所以要上浮操作'''
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize+=1
        self.percUp(self.currentSize)
    def percUp(self,i):
        while i//2>0:
            if self.heapList[i//2]>self.heapList[i]:
                self.heapList[i//2],self.heapList[i]=self.heapList[i],self.heapList[i//2]
                i//=2
            else:
                break
    def findMin(self):
        return self.heapList[1]
    '''delMin:为了保证根节点是最小的，使用下沉操作，跟左右节点中小的互换，直至最后'''
    def delMin(self):
        retval=self.heapList[1]
        self.heapList[1]=self.heapList[-1]
        self.heapList.pop()
        self.currentSize-=1
        self.percDown(1)
        return retval
    def percDown(self,i=1):
        while i*2<=self.currentSize:
            mc=self.minchild(i)
            if self.heapList[i]>self.heapList[mc]:
                self.heapList[mc],self.heapList[i]=self.heapList[i],self.heapList[mc]
                i=mc
            else:
                break
    def minchild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
    def isEmpty(self):
        pass
    def size(self):
        pass
    def buildHeap(self,list):
        pass
    '''堆排序算法：不停输出最小的'''
    def heapSort(self):
        result=[]
        for i in range(self.currentSize):
            result.append(self.delMin())
        return result

    def show(self,i=1,nt=0):
        if i<=self.currentSize:
            self.show(i*2,nt+1)
            print('\t'*nt,self.heapList[i])
            self.show(i*2+1,nt+1)



bh=BinaryHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)
bh.show()
print(bh.heapSort())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())