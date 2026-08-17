class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_water = 0

        while i < j:
            width = j - i
            height = min(heights[i], heights[j])
            if width * height > max_water:
                max_water = width * height
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_water