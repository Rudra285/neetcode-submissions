class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        for i in range(1, len(nums)):
            suffix[len(nums) - i - 1] = nums[len(nums) - i] * suffix[len(nums) - i]
        
        results = [1] * len(nums)
        for i in range(len(nums)):
            results[i] = prefix[i] * suffix[i]
        
        return results
