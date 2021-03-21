from fundamentals.test_time import test_time

'''
问题转换：
(a*b)%c = (a%c)(b%c)%c
->
(a*b*c)%d = (a*b%d)(c%d)%d=((a%d)*(b%d)%d)(c%d)%d
证明：
    a=Ac+B
    b=Cc+D
    a*b = ACcc + (AD+BC)c +BD
    a*b%c= BD%c = (a-Ac)(b-Cc)%c=(a%c)(b%c)%c
'''


class Solution():
    def __init__(self):
        pass

    @test_time
    def superPow(self, a, b):
        '''
        a**1564=a**4 * (a**126)**10
        需要一个解决 a**n的函数！
        '''

        def pow(a, n):
            ''' (a%base)*(a%base)*(a%base)...*(a%base) %base '''
            a_mod_base = a % base
            res = 1
            while n > 0:
                res *= a_mod_base
                res %= base
                n -= 1
            return res

        def my_pow(a, b):
            if len(b) == 1:
                return pow(a, b[0])
            else:
                part1 = pow(a, b.pop(-1))
                part2 = pow(my_pow(a, b), 10)
                return (part1 * part2) % base

        base = 1337
        return my_pow(a,b)
    def main(self):
        a = 2147483647
        b = [2, 0, 0]
        self.superPow(a, b.copy())


if __name__ == '__main__':
    SL = Solution()
    SL.main()
