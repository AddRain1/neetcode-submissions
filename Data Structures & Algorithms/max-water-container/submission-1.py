class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        maxArea = 0
        while l < r:
            width = abs(l - r)
            height = min(heights[l], heights[r])
            area = width * height
            if area > maxArea:
                maxArea = area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
            