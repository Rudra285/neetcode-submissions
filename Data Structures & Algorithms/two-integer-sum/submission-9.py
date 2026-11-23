class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped_nums = dict()
        for i, e in enumerate(nums):
            if target - e in mapped_nums:
                return [mapped_nums[target-e], i]
            mapped_nums[e] = i