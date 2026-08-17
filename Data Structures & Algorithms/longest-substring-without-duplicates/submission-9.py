class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        longest = ''
        for i in s:
            if i in longest:
                reset_i = longest.find(i)
                max_size = max(max_size, len(longest))
                longest = longest[reset_i + 1:]
            longest += i
        return max(max_size, len(longest))