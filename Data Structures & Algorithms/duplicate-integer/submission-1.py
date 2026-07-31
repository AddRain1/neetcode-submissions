class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for num in nums:
            dups.add(num)
        return len(dups) != len(nums)