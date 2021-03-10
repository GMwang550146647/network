from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def checkInclusion(self, s1, s2):
        window = {}
        need = {}
        for item in s1:
            need[item] = need.get(item, 0) + 1
            if item not in window: window[item] = 0
        need_size = len(need)
        length = 10 ** 5
        start = 0
        left = 0
        right = 0
        valid = 0
        while (right < len(s2)):
            # 1.当条件不符合的时候不停地扩大右边(遇到在need中的目标对象就增加计数，一旦某个字母符合要求就增加valid)
            new_c = s2[right]
            right += 1
            if new_c in need:
                window[new_c] += 1
                if window[new_c] == need[new_c]:
                    valid += 1
            # 2.当条件符合的时候开始收缩左边
            while (right-left ==len(s1)):
                # 如果更好的解，记录下来
                if valid==len(need):
                    return True
                del_c = s2[left]
                left += 1
                if del_c in need:
                    if window[del_c] == need[del_c]:
                        valid -= 1
                    window[del_c] -= 1
        return False

    def main(self):
        s = "abc"
        t = "eidbacocooo"
        self.checkInclusion(s, t)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
