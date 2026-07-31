class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search by row
        # for each row check if target
        row, col = len(matrix), len(matrix[0])

        cor_row = -1
        top, bot = 0, row - 1
        while top <= bot:
            midrow = (top + bot) // 2
            if target > matrix[midrow][-1]:
                top = midrow + 1
            elif target < matrix[midrow][0]:
                bot = midrow - 1
            else:
                cor_row = (top + bot) // 2
                break

        if not (top <= bot) or cor_row == -1:
            return False

        l, r = 0, col-1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[cor_row][m]:
                l = m + 1
            elif target < matrix[cor_row][m]:
                r = m - 1
            else:
                return True
            
        return False
