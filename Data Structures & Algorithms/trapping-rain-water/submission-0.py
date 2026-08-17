class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = 0
        max_left = 0
        max_right = 0

        while left < right:
            
            if height[left] <= height[right]:
                if max_left - height[left] > 0:
                    total += max_left - height[left]
                max_left = max(height[left], max_left)
                left += 1
            else:
                if max_right - height[right] > 0:
                    total += max_right - height[right]
                max_right = max(height[right], max_right)
                right -= 1
        return total