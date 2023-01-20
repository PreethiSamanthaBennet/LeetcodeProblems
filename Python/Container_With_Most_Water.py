class Solution(object):
    def maxArea(self, height):
        max_area = -maxsize
        left = 0
        right = len(height) - 1
        
        while left < right:
            shorter_line = min(height[left], height[right])
            max_area = max(max_area, shorter_line * (right - left))

            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1

        return max_area
