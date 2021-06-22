class student():
    num=100
    def __init__(self):
        self.name=199
    @classmethod
    def test(cls):
        print(cls.num)
    def test1(self):
        print(self.name)
student().test()
s1=student()
s1.num=199999
s1.test()
print(student.num)
print(s1.num)