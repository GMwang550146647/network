from common import cal_min_common_multiplier

S = 321
E = 5
D = 29
N = 323
tempt = 1
for i in range(D):
    tempt = (tempt * S ** E) % N
    print(tempt)


def cal_factor(num):
    """
    求出该num的所有除得尽的数字
    """
    result = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            result.append(i)
    return result


def cal_min_common_multiplier(a, b):
    """
    求a和b的最小公倍数
    """

    def max_common_m(a, b):
        a, b = (a, b) if a > b else (b, a)
        while a % b != 0:
            a, b = b, a % b
        return b

    return a * b // max_common_m(a, b)


def cal_multipliers(num):
    """
    返回该num是由哪些数相乘而来
    """
    result = []
    while num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                result.append(i)
                num //= i
    return result


def tell_zhishu(num):
    """
    判断是否质数
    """
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True

    # 如果输入的数字小于或等于 1，不是质数
    else:
        return False


def cal_D(N, E):
    """
    破解出D
    """
    factors = cal_factor(N)
    factors = [item for item in factors if tell_zhishu(item)]
    for fi in factors:
        fj = N // fi
        L = cal_min_common_multiplier(fi - 1, fj - 1)
        print((set(cal_multipliers(E)), set(cal_multipliers(L))), )
        if not (set(cal_multipliers(E)) & set(cal_multipliers(L))):
            print('yr', (set(cal_multipliers(E)), set(cal_multipliers(L))), L)
            for i in range(100000):
                if (i * E) % L == 1:
                    return i
    return None


if __name__ == '__main__':
    print(cal_factor(323))
    print(cal_multipliers(323))
    print(cal_D(N, E))
    print(323 / 17)
