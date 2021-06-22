gm="gmwang"

def func(gm):
    print(gm,"是个帅哥")
class A():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return "name:%s,age:%d"%(self.name,self.age)

'''1.执行谁，谁就是__main__，当被import的时候不会被执行'''
if __name__=="__main__":
    print("main里面")
    a=A("gm",10)
    print(a)

'''2.该文件被import的时候会执行'''
print(__name__) #__main__


'''3.前面有"_"的变量和函数不能被其他包调用'''
def _hiddenFunc():
    print("you can't 调用我")

'''4.规定外面的文件只能访问到这两个变量'''
gmnotinall=99999
__all__=['gm','A','func']