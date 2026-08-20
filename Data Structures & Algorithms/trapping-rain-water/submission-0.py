class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                change = leftMax - height[l]
                if change > 0:
                    res += change
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                change = rightMax - height[r]
                if change > 0:
                    res += change
        return res