class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights) -1
        max_area = 0
        while (left < right):
            temp = (min(heights[left] , heights[right]) * (right - left))
            if temp > max_area:
                max_area = temp
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area