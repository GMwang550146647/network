"""
yield : 返回一个值
yield : 返回一个生成器对应的各个值
"""
def my_generator(s,e):
    for i in range(s,e):
        yield i

def get_generator_raw():
    yield 1
    yield 2
    yield [3,4,5]
    yield (6,7,8)
    yield my_generator(9,12)

def get_generator():
    yield 1
    yield 2
    yield from [3,4,5]
    yield from (6,7,8)
    yield from my_generator(9,12)

if __name__ == '__main__':
    for item in get_generator_raw():
        print(item)
    print("#######################")
    for item in get_generator():
        print(item)