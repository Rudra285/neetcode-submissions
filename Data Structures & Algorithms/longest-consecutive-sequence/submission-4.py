class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        temp = 1
        for i in nums:
            if i - 1 not in nums:
                longest = max(temp, longest)
                j = i
                temp = 1
                while j + 1 in nums:
                    j += 1
                    temp += 1
        longest = max(temp, longest)
        return longest
            

            