'''

4.简单加减乘除运算：
步骤：
1.把符号和数字切分开
2.操作符移到左括号（前缀）或者移到右括号（后缀）
3.计算前缀或者后缀的结果


'''

import re
expression="4+(20*3+7)-30/3"
class calculator():
    def __init__(self,expression):
        self.expression=expression
        #定义运算的优先级
        self.prec={'*':3,'/':3,'+':2,'-':2,'(':1}
        self.calFun=['+','-','*','/']
    '''
    1.第一步：把字符串拆分为list：
    ['4', '+', '(', '20', '*', '3', '+', '7', ')', '-', '30', '/', '3']
    '''
    def split(self):
        expList=re.split(r'(\w+|\(|\))', self.expression)
        expList=list(filter(lambda a:a!='',expList))
        return expList
    '''
    2.第二步：转化为后缀模式
    '''
    def convert2Backward(self,expList):
        outputList=[]
        opstack=[]
        numPattern=re.compile(r'\d+')
        for exp in expList:
            print(exp)
            #1.对于数字，直接加入ouputList
            if len(re.findall(numPattern,exp))==1:
                outputList.append(exp)
            #对于左括号，直接入栈
            elif exp =='(':
                topToken=opstack.append(exp)
            #对于右括号，把栈里面的符号输出，直至遇到左括号
            elif exp==')':
                toptoken=opstack.pop()
                while toptoken!='(':
                    outputList.append(toptoken)
                    toptoken=opstack.pop()
            #对于运算符：若后一个运算符比前一个运算符优先级低，就output前面全部的高级的运算符，再加入当前运算符到栈
            else:
                while(len(opstack)>0 and self.prec[opstack[-1]]>=self.prec[exp]):
                    outputList.append(opstack.pop())
                opstack.append(exp)
            print('opstack:',opstack)
            print('outputList:',outputList)
            print("~~~~~~~~~~~~~~~~~~~~~")
        #最后把栈中的剩余操作符弹出
        while len(opstack)>0:
            outputList.append(opstack.pop())
            print(opstack)
            print(outputList)
            print("~~~~~~~~~~~~~~~~~~~~~")
        print(outputList)
        return outputList
    '''第三步：计算前缀或者后缀的结果'''
    def calBackward(self,backward):
        calList=[]
        for exp in backward:
            if exp not in self.calFun:
                calList.append(exp)
            else:
                nex = float(calList.pop())
                pre = float(calList.pop())
                if exp=='+':
                    calList.append(pre+nex)
                if exp=='-':
                    calList.append(pre - nex)
                if exp=='*':
                    calList.append(pre * nex)
                if exp=='/':
                    calList.append(pre / nex)
        return calList[0]
    def main(self):
        try:
            expList=self.split()
            backward=self.convert2Backward(expList)
            result=self.calBackward(backward)
            print(result)
        except Exception as err:
            print(err)
            print("Wrong Expression")


cal=calculator(expression)
cal.main()

'''
结果范例：
['4', '+', '(', '20', '*', '3', '+', '7', ')', '-', '30', '/', '3']
opstack: []
outputList: ['4']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['+']
outputList: ['4']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['+', '(']
outputList: ['4']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['+', '(']
outputList: ['4', '20']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['+', '(', '*']
outputList: ['4', '20']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['+', '(', '*']
outputList: ['4', '20', '3']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['+', '(', '+']
outputList: ['4', '20', '3', '*']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['+', '(', '+']
outputList: ['4', '20', '3', '*', '7']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['+']
outputList: ['4', '20', '3', '*', '7', '+']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['-']
outputList: ['4', '20', '3', '*', '7', '+', '+']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['-']
outputList: ['4', '20', '3', '*', '7', '+', '+', '30']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['-', '/']
outputList: ['4', '20', '3', '*', '7', '+', '+', '30']
~~~~~~~~~~~~~~~~~~~~~
opstack: ['-', '/']
outputList: ['4', '20', '3', '*', '7', '+', '+', '30', '3']
~~~~~~~~~~~~~~~~~~~~~
['-']
['4', '20', '3', '*', '7', '+', '+', '30', '3', '/']
~~~~~~~~~~~~~~~~~~~~~
[]
['4', '20', '3', '*', '7', '+', '+', '30', '3', '/', '-']
~~~~~~~~~~~~~~~~~~~~~
['4', '20', '3', '*', '7', '+', '+', '30', '3', '/', '-']
'''