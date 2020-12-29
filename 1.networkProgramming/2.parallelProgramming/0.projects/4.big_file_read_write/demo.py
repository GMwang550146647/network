import os
from threading import Thread, current_thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio
from tqdm import tqdm
import time
from functools import reduce
import math
class BigFileIO():
    def __init__(self):
        self.input_dir = 'input'
        self.output_dir = 'output'
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def time_it(self, func, args):
        now = time.time()
        func(**args)
        return round((time.time() - now), 2)

    def create_big_file(self, n_batch=100, batch_size=10000, file_name='data3.txt', encoding='utf-8', mode='w'):
        template = "{} th line: HaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHa!"
        with open(os.path.join(self.input_dir, file_name), mode=mode,
                  encoding=encoding if encoding != 'byte' else None) as f:
            for i in range(n_batch):
                contenti = []
                for j in range(batch_size):
                    contenti.append(template.format(n_batch * i + j))
                if encoding == 'byte':
                    f.write('\n'.join(contenti).encode())
                    if i != n_batch - 1:
                        f.write(b'\n')
                else:
                    f.write(('\n'.join(contenti).encode().decode(encoding)))
                    if i != n_batch - 1:
                        f.write('\n'.encode().decode(encoding))
                print("{} batch finished".format(i))

    def read_big_file(self, file_name='data.txt'):
        file = os.path.join(self.input_dir, file_name)
        output_file = os.path.join(self.output_dir, 'normal_' + file_name)
        with open(file,'rb') as f:
            content = f.read()
        with open(output_file,'wb') as f:
            f.write(content)

    def read_big_file_multi_thread(self, n_tasks=128,buffer_size = 1024*1024*128, file_name='data.txt'):
        def read_file(kwargs):
            file = kwargs.get('file')
            start = kwargs.get('start', 0)
            buffer_size = kwargs.get('buffer_size', 1024 * 1024 * 10)
            with open(file, 'rb') as f_in:
                f_in.seek(start)
                return f_in.read(buffer_size)

        result = b''
        file = os.path.join(self.input_dir, file_name)
        file_size=os.path.getsize(file)
        n_divisions=math.ceil(file_size/float(n_tasks*buffer_size))
        output_file = os.path.join(self.output_dir, 'thread_'+file_name)

        position = 0
        for i in range(n_divisions):
            tasks = [{'file': file, 'start': position + buffer_size * i, 'buffer_size': buffer_size} for i in
                     range(n_tasks)]
            with ThreadPoolExecutor() as executor:
                resulti = [resp for resp in tqdm(executor.map(read_file, tasks), total=len(tasks))]
                resulti=reduce(lambda a, b: a + b, resulti)
                result+=resulti
            position += buffer_size * n_tasks
            with open(output_file,'ab') as f_out:
                f_out.write(result)

    def read_big_file_multi_coroutines(self, n_threads=100, n_splits=10000, file_name='data1.txt'):
        # async def conroutines_read( f):
        #     await asyncio.(f)
        pass

    def save_big_file(self):
        pass

    def run(self):
        # 1.create files
        # create_data_params = [
        #     {'file_name': 'byte_data_small.txt', 'batch_size': 10000, 'encoding': 'byte', 'mode': 'wb'},
        #     {'file_name': 'byte_data_medium.txt', 'batch_size': 100000, 'encoding': 'byte', 'mode': 'wb'},
        #     {'file_name': 'byte_data_large.txt', 'batch_size': 1000000, 'encoding': 'byte', 'mode': 'wb'},
        #     {'file_name': 'utf8_data_small.txt', 'batch_size': 10000, 'encoding': 'utf-8', 'mode': 'w'},
        #     {'file_name': 'utf8_data_medium.txt', 'batch_size': 100000, 'encoding': 'utf-8', 'mode': 'w'},
        #     {'file_name': 'utf8_data_large.txt', 'batch_size': 1000000, 'encoding': 'utf-8', 'mode': 'w'},
        #     {'file_name': 'gbk_data_small.txt', 'batch_size': 10000, 'encoding': 'GBK', 'mode': 'w'},
        #     {'file_name': 'gbk_data_medium.txt', 'batch_size': 100000, 'encoding': 'GBK', 'mode': 'w'},
        #     {'file_name': 'gbk_data_large.txt', 'batch_size': 1000000, 'encoding': 'GBK', 'mode': 'w'},
        # ]
        # for parami in create_data_params:
        #     self.create_big_file(**parami)

        # 2.read files
        file_names = [
            'byte_data_small.txt',
            'byte_data_medium.txt',
            # 'byte_data_large.txt'
        ]
        for filei in file_names:
            t1i = self.time_it(self.read_big_file_multi_thread, {'file_name':filei})
            print("Read_big_file_multi_thread  file  {}   ->Time:  {}s".format(filei, t1i))
            t2i = self.time_it(self.read_big_file, {'file_name':filei})
            print("Read_file_python_build_i   file  {}   ->Time:  {}s".format(filei, t2i))


if __name__ == '__main__':
    BigFileIO().run()
