class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def backtrack(start):
            res.append(path[:])          # record current subset (copy!)
            for i in range(start, len(nums)):
                path.append(nums[i])     # choose
                backtrack(i + 1)         # explore the elements after i
                path.pop()               # un-choose

        backtrack(0)
        return res
