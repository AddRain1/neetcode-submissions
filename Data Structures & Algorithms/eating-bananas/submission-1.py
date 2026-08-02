class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max k will be largest int
        # binary search from 1 to max k
        max_k = max(piles)
        l, r = 1, max_k

        res = r

        while l <= r:
            m = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / m)
            if time <= h:
                res = m
                r = m - 1
            elif time > h:
                l = m + 1

        return res

