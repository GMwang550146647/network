from threading import  Thread

class MyThread(Thread):
    def __init__(self,data):
        self.data=data
        super().__init__()

    def run(self):
        print("process {} received data :{}".format(self.ident,self.data))

if __name__ == '__main__':
    t=MyThread("gmwang")
    t.start()
    print(t.ident)