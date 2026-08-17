class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        for right in range(len(temperatures)):
            left = right
            while left < len(temperatures) and temperatures[right] >= temperatures[left]:
                left += 1
            if left < len(temperatures):
                res[right] = left - right
        
        return res