'''
核心：
    门面相当于项目经理，底下管理很多工具人，对外和客户谈需求，客户只需要通过项目经理从而调动各种工具人
'''
"""
1.门面（客户端和服务提供端的接口）
"""


class EventManager(object):
    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")

    def arrange(self):
        self.hostelier = Hotelier()
        self.hostelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


"""
2.客户端
"""


class You():
    def __init__(self):
        print("You:: Whoa! Marriage Arrangements??!!!")

    def askEventManager(self):
        print("You:: Let's Contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")


"""
3.子系统（功能的提供商）
"""


class Hotelier():
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")

    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the booking \n\n")


class Florist():
    def __init__(self):
        print("Flower Decorations for the Event? --")

    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations \n\n")


class Caterer():
    def __init__(self):
        print("Food Arrangements for the Event --")

    def setCuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n")


class Musician():
    def __init__(self):
        print("Musical Arrangements for the Marriage --")

    def setMusicType(self):
        print("Jazz and Classical will be played\n\n")


if __name__ == '__main__':
    you = You()
    you.askEventManager()
