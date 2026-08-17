class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = ''
        for i in range(len(s)):
            if s[i] in window:
                k = window.index(s[i])
                longest = max(longest, len(window))
                window = window[k + 1:i]
            window += s[i]
        return max(longest, len(window))