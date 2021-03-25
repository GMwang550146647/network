def Singleton(cls):
    _instance = {}
    count = 0

    def _singleton(*args, **kwargs):
        nonlocal count
        if cls not in _instance:
            print(f"{count} : Initial cls ->              {cls}")
            _instance[cls] = cls(*args, **kwargs)
        else:
            print(f"{count} : Cls already initialized ->  {cls}")
        count += 1
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


if __name__ == '__main__':
    a1 = A(1)
    a2 = A(2)
    print(f"a1 id: {id(a1)}, a1 value: {a1.x}")
    print(f"a2 id: {id(a2)}, a2 value: {a2.x}")
