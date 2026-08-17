class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest = 1
        curr = 1
        nums = list(set(nums))
        nums.sort()

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            if i > 0 and abs(nums[i - 1] - nums[i]) == 1:
                curr += 1
                if curr > largest:
                    largest = curr
            elif i > 0 and abs(nums[i - 1] - nums[i]) > 1:
                curr = 1

        return largest
