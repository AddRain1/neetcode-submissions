class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search by row
        # for each row check if target
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            if target > matrix[i][col-1] or target < matrix[i][0]:
                continue
            l, r = 0, col-1
            while l <= r:
                m = (l + r) // 2
                if target > matrix[i][m]:
                    l = m + 1
                elif target < matrix[i][m]:
                    r = m - 1
                else:
                    return True
            
        return False
