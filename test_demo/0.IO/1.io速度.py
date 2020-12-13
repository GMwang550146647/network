import time
def time_it(func, args):
    now = time.time()
    func(**args)
    return round((time.time() - now)*1000,3)
class IOTest():
    def read_write_file(self,n):
        for i in range(n):
            with open('data.txt') as f:
                data=int(f.read())+1
            with open('data.txt','w') as f:
                f.write(str(data))
    def modify_memory(self,n):
        a=0
        for i in range(n):
            a+=1
    def print_func(self,n):
        a=0
        for i in range(n):
            a+=1
            print(a)
    def run(self,n_times=10000):
        t1=time_it(self.read_write_file,{"n":n_times})
        t2=time_it(self.print_func,{"n":n_times})
        t3=time_it(self.modify_memory,{"n":n_times})
        print("read_write variable from file {} times : {} ms ".format(n_times,t1))
        print("Print variable {} times                : {} ms ".format(n_times,t2))
        print("Modify momory variable {} times        : {} ms ".format(n_times,t3))
if __name__ == '__main__':
    IOTest().run()