class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left <= right:
            width = right - left

            if heights[left] <= heights[right]:
                max_area = max(max_area, width * heights[left])
                left += 1
            else:
                max_area = max(max_area, width * heights[right])
                right -= 1
        
        return max_area