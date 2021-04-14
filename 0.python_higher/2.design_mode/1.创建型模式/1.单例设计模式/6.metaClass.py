
class SingletonBase(type):
    _instance=None
    def __init__(self,*args,**kwargs):
        print("SingletonBase init")
        super(SingletonBase, self).__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("SingletonBase call")
        if self._instance is None:
            self._instance=super().__call__(*args,**kwargs)
        return self._instance
    def __new__(cls, *args, **kwargs):
        print("SingletonBase new")
        return super().__new__(cls,*args,**kwargs)

class Singleton(metaclass=SingletonBase):
    def __init__(self):
        print("Singleton init")
    def __new__(cls, *args, **kwargs):
        print("Singleton new")
        return super().__new__(cls)

if __name__ == '__main__':
    s1=Singleton()
    s2=Singleton()
    print(s1==s2)