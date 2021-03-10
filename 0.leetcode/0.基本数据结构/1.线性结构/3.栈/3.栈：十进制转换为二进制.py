num=1000
def convert2Binary(num):
    mystack=[]
    while(num!=0):
        currentBit=num%2
        num//=2
        mystack.append(currentBit)
    mylist=[]
    for i in range(len(mystack)):
        mylist.append(mystack.pop())
    return mylist




print(convert2Binary(num))