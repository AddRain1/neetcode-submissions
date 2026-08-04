class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack
        # keeps decreasing order, if a bigger number joins, pop everything it can get to

        res = [0] * len(temperatures)

        stack = [] # [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append([t, i])
        
        return res
