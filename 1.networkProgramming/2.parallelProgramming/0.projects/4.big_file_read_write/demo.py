import os
from threading import Thread,current_thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio
from tqdm import tqdm
import time
from functools import reduce
class BigFileIO():
    def __init__(self):
        self.input_dir = 'input'
        self.output_dir = 'output'

    def time_it(self,func, args):
        now = time.time()
        func(**args)
        return round((time.time() - now), 2)

    def create_big_file(self, n_batch=100, batch_size=10000, file_name='data1.txt'):
        template = "第{}行：哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈"
        with open(os.path.join(self.input_dir, file_name), 'w') as f:
            for i in range(n_batch):
                contenti = []
                for j in range(batch_size):
                    contenti.append(template.format(n_batch * i + j))
                f.write('\n'.join(contenti))
                print("{} batch finished".format(i))
                if i != n_batch - 1:
                    f.write('\n')
    def read_big_file(self,file_name='data.txt'):
        file = os.path.join(self.input_dir, file_name)
        with open(file) as f:
            content=f.read()

    def read_big_file_multi_thread(self, n_pertask=1000,file_name='data.txt'):
        def read_file(kwargs):
            file=kwargs.get('file')
            start=kwargs.get('start',0)
            buffer_size=kwargs.get('buffer_size',1024*1024*10)
            file.seek(start)
            return file.read(buffer_size)
        result=[]
        file = os.path.join(self.input_dir, file_name)
        with open(file,'rb') as f:
            position=0
            while True:
                buffer_size=1024*1024*10
                tasks=[{'file':f,'start':position+buffer_size*i,'buffer_size':buffer_size} for i in range(n_pertask)]
                with ThreadPoolExecutor() as executor:
                    resulti=[resp for resp in tqdm(executor.map(read_file, tasks), total=len(tasks))]
                    result+=resulti
                position += buffer_size * n_pertask
                if resulti[-1]==b"":
                    break
            result=reduce(lambda a,b:a+b,result).decode('utf-8')

    def read_big_file_multi_coroutines(self,n_threads=100, n_splits=10000,file_name='data1.txt'):
        # async def conroutines_read( f):
        #     await asyncio.(f)
        pass
    def save_big_file(self):
        pass
    def run(self):
        # self.create_big_file()
        t1=self.time_it(self.read_big_file_multi_thread,{})
        print("Read_big_file_multi_thread Time:  {}s".format(t1))
        t2=self.time_it(self.read_big_file,{})
        print("Read_big_file_multi_thread Time:  {}s".format(t2))

if __name__ == '__main__':
    BigFileIO().run()
