from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def minWindow(self, s, t):
        window = {}
        need = {}
        for item in t:
            need[item] = need.get(item, 0) + 1
            if item not in window: window[item] = 0
        need_size = len(need)
        length = 10 ** 5
        start = 0
        left = 0
        right = 0
        valid = 0
        while (right < len(s)):
            # 1.当条件不符合的时候不停地扩大右边(遇到在need中的目标对象就增加计数，一旦某个字母符合要求就增加valid)
            new_c = s[right]
            right += 1
            if new_c in need:
                window[new_c] += 1
                if window[new_c] == need[new_c]:
                    valid += 1
            # 2.当条件符合的时候开始收缩左边
            while (valid == need_size):
                # 如果更好的解，记录下来
                if right - left < length:
                    length = right - left
                    start = left
                del_c = s[left]
                left += 1
                if del_c in need:
                    if window[del_c] == need[del_c]:
                        valid -= 1
                    window[del_c] -= 1
        return "" if length == 10 ** 5 else s[start:(start + length)]

    def main(self):
        s = "aa"
        t = "aa"
        self.minWindow(s, t)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
