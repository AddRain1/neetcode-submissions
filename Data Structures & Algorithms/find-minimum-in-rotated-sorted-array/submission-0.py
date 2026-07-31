class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("infinity")
        l, r = 0, len(nums) - 1


        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                return res
            else:
                mid = (l + r) // 2
                res = min(res, nums[mid])
                if nums[mid] >= nums[l]:
                    l = mid + 1
                elif nums[mid] <= nums[r]:
                    r = mid - 1

                


            