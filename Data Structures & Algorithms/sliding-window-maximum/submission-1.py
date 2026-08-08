from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        l = 0
        res = []
        for r in range(len(nums)):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
                
            queue.append(r)
            if queue[0] < l:
                queue.popleft()

            # when window gets too big
            if r - l + 1 == k:
                res.append(nums[queue[0]])
                l += 1
                
        return res