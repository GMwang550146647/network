class Borg:
    __shared_state = {1: 2}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


if __name__ == '__main__':
    b = Borg()
    b1 = Borg()
    b1.x = 4
    print("Borg b:{}".format(b))
    print("Borg b1:{}".format(b1))
    print("Object State b:{}".format(b.__dict__))
    print("Object State b1:{}".format(b1.__dict__))
