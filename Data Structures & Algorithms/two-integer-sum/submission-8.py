class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()

        for i, e in enumerate(nums):
            if target - e in visited:
                return [visited[target - e], i]
            
            visited[e] = i
        