from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def findAnagrams(self, s, p):
        window = {}
        needs = {}
        for item in p:
            window[item] = 0
            needs[item] = needs.get(item, 0) + 1
        valid = 0
        all_pos = []
        left = 0
        right = 0
        len_p = len(p)
        len_needs = len(needs)
        while (right < len(s)):
            # 1.右指针向前
            new_char = s[right]
            right += 1
            if new_char in needs:
                window[new_char] += 1
                if window[new_char] == needs[new_char]:
                    valid += 1
            # 2.左指针向前
            while (right - left == len_p):
                if (valid == len_needs):
                    all_pos.append(left)
                del_char = s[left]
                left += 1
                if del_char in needs:
                    if needs[del_char] == window[del_char]:
                        valid -= 1
                    window[del_char] -= 1
        return all_pos

    def main(self):
        s = "cbaebabacd"
        p = "abc"
        self.findAnagrams(s, p)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
