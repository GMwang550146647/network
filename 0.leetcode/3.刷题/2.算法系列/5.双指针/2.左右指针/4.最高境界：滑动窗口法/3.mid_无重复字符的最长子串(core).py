from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0
        right = 0
        max_length = -1
        while (right < len(s)):
            new_char = s[right]
            right+=1
            window[new_char] = window.get(new_char, 0) + 1
            while (window[new_char] > 1):
                del_char = s[left]
                left += 1
                window[del_char] -= 1
            if right - left > max_length:
                max_length = right - left
        return max_length

    def main(self):
        s = "pwwkew"
        self.lengthOfLongestSubstring(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
