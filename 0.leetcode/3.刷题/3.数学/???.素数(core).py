from fundamentals.test_time import test_time
import math

"""
寻找 [2,n)范围的素数
"""


class Solution():
    def __init__(self):
        pass

    @test_time
    def countPrimes(self, n):
        """
        从2 计算到 n**0.5
        """
        def isPrime(n):
            i = 2
            while (i ** 2 <= n):
                if n % i == 0:
                    return False
                i += 1
            return True

        count = 0
        primes = []
        for i in range(2, n):
            if isPrime(i):
                count += 1
                primes.append(i)

        return count, primes

    @test_time
    def countPrimes_Sieve_of_Eratoshthenes(self, n):
        """
        从2 计算到 n**0.5，每找到一个素数，马上将其在n之前的倍数干掉！
        """
        isPrime = [True for _ in range(n)]
        for i in range(2, math.ceil(n ** 0.5) + 1):
            if (isPrime[i]):
                for j in range(i ** 2, n, i):
                    isPrime[j] = False
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count

    def main(self):
        nums = 11
        self.countPrimes(nums)
        self.countPrimes_Sieve_of_Eratoshthenes(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
