class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            prod = 1
            for ind, num in enumerate(nums):
                if i == ind:
                    continue
                prod *= num
            res.append(prod)
        return res
