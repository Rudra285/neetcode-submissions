class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped_nums = {}
        for i, e in enumerate(nums):
            remaining = target - e
            if remaining in mapped_nums:
                return [mapped_nums[remaining], i]
            mapped_nums[e] = i