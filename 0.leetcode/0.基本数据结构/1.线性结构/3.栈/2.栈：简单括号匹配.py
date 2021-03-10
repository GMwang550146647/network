class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
def parChecker(symbolString):
    strStack=Stack()
    convert={')':'(','}':'{',']':'['}
    for i in range(len(symbolString)):
        if symbolString[i]in['(','{','[']:
            strStack.push(symbolString[i])
        elif symbolString[i]in convert.keys():
            if strStack.size()>0:
                if strStack.pop()!=convert[symbolString[i]]:
                    return False
            else:
                return False
    if strStack.size()==0:
        return True
    else:
        return False

expressions=["(2+4)*(6+8)","([(2+4)]*)(6+8)","([(2+4)*)](6+8)","(2+4)*(6+8))"]
for item in expressions:
    print(parChecker(item))
