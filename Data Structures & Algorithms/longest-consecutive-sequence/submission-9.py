class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 1

        if not nums:
            return 0

        for i in nums:
            if i - 1 not in nums:
                j = i
                temp = 1
                while j + 1 in nums:
                    j += 1
                    temp += 1
                longest = max(longest, temp)
        
        return longest