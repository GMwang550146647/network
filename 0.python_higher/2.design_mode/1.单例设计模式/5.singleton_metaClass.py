class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("****Here is myInt!")
        print("Do whatever you want with these objects")
        print("args:{},kwargs:{}".format(args,kwargs))
        return type.__call__(cls)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class MetaSingleton(type):
    _instance={}
    def __call__(self, *args, **kwargs):
        if clas

if __name__ == '__main__':
    i=int(4,5)
    print(i.x)