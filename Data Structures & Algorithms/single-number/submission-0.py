class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = set()
        for i in nums:
            if i not in visited:
                visited.add(i)
            else:
                visited.remove(i)
        return list(visited)[0]
        