class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size_nums = len(nums)
        p = [1] * size_nums
        s = [1] * size_nums

        for i in range(1, size_nums):
            p[i] = nums[i - 1] * p[i - 1]
        for i in range(size_nums - 2, -1, -1):
            s[i] = s[i + 1] * nums[i + 1]
        res = [1] * size_nums
        for i in range(size_nums):
            res[i] = p[i] * s[i]
        return res
