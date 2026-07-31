class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bums = set(nums)
        return len(bums) < len(nums)