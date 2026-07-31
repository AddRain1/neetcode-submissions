class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # initilize max_length
        max_length = 0
        # make nums a set to remove duplicates
        nums_set = set(nums)

        # iterate through each num in nums_set, and see if it has a left neighbor
        # we know that every element without a left neighbor is the start
        # of a sequence
        for num in nums_set:
            if (num-1) not in nums_set:
                length = 0
                while num + length in nums_set:
                    length += 1
                max_length = max(max_length, length)
        
        return max_length

