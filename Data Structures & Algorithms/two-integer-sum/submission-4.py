class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, e in enumerate(nums):
            remaining = target - e
            if remaining in seen:
                return [seen[remaining], i]
            seen[e] = i