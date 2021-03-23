from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    # @test_time
    def movingCount(self, m, n, k):
        def arr_sum(n):
            if n < 0:
                return 0
            else:
                return int(n * (n + 1) / 2)

        def mn_tri(m, k):
            '''
            计算三角形
            '''
            k = min(19, k)
            if m <= k:
                m_tri=arr_sum(k-min(9,m))
            else:
                m_tri= 0 if k<=9 else arr_sum(k-9)
            return m_tri

        def count_cur_area(m, n, k):
            '''
            计算三角形面积的
            '''
            if  k>=min(m,10)+min(n,10)-2:
                return min(m, 10) * min(n, 10)
            else:
                big_tri = arr_sum(min(20, k + 1))
                m_tri = mn_tri(m-1, k)
                n_tri = mn_tri(n-1, k)
                cur_area = big_tri - m_tri - n_tri
                return cur_area

        def count(m, n, k):
            if m <= 0 or n <= 0 or k < 0:
                return 0
            else:
                c0 = count_cur_area(m, n, k)
                c1 = count(m - 10, n, k - 1) if (m - 10, n) not in visited and k>=9 else 0
                c2 = count(m, n - 10, k - 1) if (m, n - 10) not in visited and k>=9 else 0
                visited.add((m - 10, n))
                visited.add((m, n - 10))
                return c0 + c1 + c2
        visited = set()
        return count(m, n, k)

    def main(self):
        m = 20
        n = 20
        k = 13
        print(self.movingCount(m, n, k))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
