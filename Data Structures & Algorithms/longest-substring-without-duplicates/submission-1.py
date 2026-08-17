class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        curr = ''
        for i in s:
            if i in curr:
                idx = curr.find(i)
                curr = curr[idx + 1:]
            curr += i
            if len(curr) > len(longest):
                longest = curr
        return len(longest)
