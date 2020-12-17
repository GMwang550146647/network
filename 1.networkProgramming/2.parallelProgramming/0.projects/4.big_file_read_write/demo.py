import os
from threading import Thread,current_thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio
class BigFileIO():
    def __init__(self):
        self.input_dir = 'input'
        self.output_dir = 'output'

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
    def read_big_file_multi_thread(self,n_threads=100, n_splits=10000,file_name='data1.txt'):
        pass

    def read_big_file_multi_coroutines(self,n_threads=100, n_splits=10000,file_name='data1.txt'):
        # async def conroutines_read( f):
        #     await asyncio.(f)
        pass
    def save_big_file(self):
        pass
    def run(self):
        self.create_big_file()


if __name__ == '__main__':
    BigFileIO().run()
