class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = 0
        current_sum = 0

        for i in range(len(nums) + 1):
            actual_sum += i
        
        for i in range(len(nums)):
            current_sum += nums[i]
        
        return actual_sum - current_sum