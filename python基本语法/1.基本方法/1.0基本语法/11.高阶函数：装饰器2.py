'''3.多重装饰器'''
def deco1(func):
    def wrapper(a):
        print('deco1')
        func(a)
    return wrapper
def deco2(func):
    def wrapper(a):
        print('deco2')
        func(a)
    return wrapper


#先装近的那个，这里是deco1
@deco2
@deco1
def func(a):
    print(a)

func(4)


'''
4.带参数的装饰器：多层装饰器
实质：产生装饰器的函数
'''
def decoCreater(a):
    if a=='a':
        def decorate(func):
            def wrapper(*args,**kwargs):
                print("经过修饰后的函数：")
                print('已授权')
                func(*args)
            return wrapper
        return decorate
    else:
        def decorate(func):
            def wrapper(*args,**kwargs):
                print("经过修饰后的函数：")
                print("未授权")
                func(*args)
            return wrapper
        return decorate
@decoCreater('a')   #可以根据参数产生不同的装饰器
def func(arg):
    print("原来的函数运行了:%s"%arg)

func('djsallfjaslj')


'''5.装饰器应用：付款'''
isLogin=False
def login():
    global isLogin
    name=input("please input name:")
    password=input("please input password:")
    if name=='gmwang' and password=='123456':
        isLogin=True

def loginRequire(func):
    def wrapper(*args,**kwargs):
        if not isLogin:
            while(not isLogin):
                login()
        func(args)
    return wrapper

@loginRequire
def pay(money):
    print("the amount is:%d"%money)
    print("paying...")
    print("finished!")

pay(100000)