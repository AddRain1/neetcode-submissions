class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        # if the sum is greater than target, increment larger pointer
        # return l then r

        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                if numbers[l] < numbers[r]:
                    r -= 1
                else:
                    l += 1
            if sum < target:
                if numbers[l] < numbers[r]:
                    l += 1
                else:
                    r -= 1
            if sum == target:
                return [l+1, r+1]
            