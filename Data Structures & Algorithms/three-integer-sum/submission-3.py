class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and n == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums)-1

            while j < k:
                threesum = n + nums[j] + nums[k]
                if threesum > 0:
                    k-=1
                elif threesum < 0:
                    j+=1
                else:
                    res.append([n, nums[j], nums[k]])
                    k-=1
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return res