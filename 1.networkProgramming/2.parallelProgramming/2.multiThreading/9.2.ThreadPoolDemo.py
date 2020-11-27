from concurrent import futures
from tqdm import tqdm

import pandas as pd

class MultiThread():
    @staticmethod
    def multi_thread(func,data,n_threads=100):
        """
        :param data: Dict, tuple, list or nested
        :return:
        """
        all_results = []
        if type(data) == pd.core.frame.DataFrame:
            print("Received input type:dataframe")
            data=data.reset_index(drop=True)         #This is very important!
            with futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
                data=list(data.T.to_dict().values())
                for resp in tqdm(executor.map(func,data ),total=len(data)):
                    all_results.append(resp)
            all_results = pd.DataFrame(all_results)
        elif type(data) in [tuple, list] and type(data[0]) in [tuple, list, dict]:
            print("Received input type:{} of {}".format(type(data),type(data[0])))
            with futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
                for resp in tqdm(executor.map(func, data),total=len(data)):
                    all_results.append(resp)
        elif type(data) in [tuple, list]:
            print("Received input type:{}".format(type(data)))
            with futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
                for resp in tqdm(executor.map(func, data),total=len(data)):
                    all_results.append(resp)
        else:
            print("Received input type:{}".format(type(data)))
            with futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
                for resp in tqdm(executor.map(func, data)):
                    all_results.append(resp)
        return all_results

    @staticmethod
    def decorator(n_threads):
        """
        decorator for multithread
        """
        def multi_thread_wrapper(func):
            def inner_warpper(data):
                """
                :param data: Dict, tuple, list or nested
                :return:
                """
                all_results = []
                if type(data) == pd.core.frame.DataFrame:
                    print("Received input type:dataframe")
                    data = data.reset_index(drop=True)  # This is very important!
                    with futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
                        data = list(data.T.to_dict().values())
                        for resp in tqdm(executor.map(func, data), total=len(data)):
                            all_results.append(resp)
                    all_results = pd.DataFrame(all_results)
                elif type(data) in [tuple, list] and type(data[0]) in [tuple, list, dict]:
                    print("Received input type:{} of {}".format(type(data), type(data[0])))
                    with futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
                        for resp in tqdm(executor.map(func, data), total=len(data)):
                            all_results.append(resp)
                elif type(data) in [tuple, list]:
                    print("Received input type:{}".format(type(data)))
                    with futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
                        for resp in tqdm(executor.map(func, data), total=len(data)):
                            all_results.append(resp)
                else:
                    print("Received input type:{}".format(type(data)))
                    with futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
                        for resp in tqdm(executor.map(func, data)):
                            all_results.append(resp)
                return all_results
            return inner_warpper
        return multi_thread_wrapper