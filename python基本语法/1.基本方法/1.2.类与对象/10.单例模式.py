'''
单例模式：
作用：只创建一个实例，永远都是这个实例
'''
class Singleton:
    __instance=None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

s=Singleton()
s1=Singleton()
print(s)
print(s1)