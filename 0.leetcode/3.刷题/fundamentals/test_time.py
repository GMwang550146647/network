import time


def test_time(func, test_times=100):
    def wrapper(*args, **kwargs):
        # 计时
        start = time.process_time()
        for i in range(test_times):
            result = func(*args, **kwargs)
        elapsed = (time.process_time() - start)
        print(func.__name__, ":")
        print("Time used:", elapsed)
        print("Result:", result)
        return result

    return wrapper
