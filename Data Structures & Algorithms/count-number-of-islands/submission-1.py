class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        visited = []

        def dfs(r, c):
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if (r < 0 or c >= col or r >= row or 
                c < 0 or grid[r][c] == "0" or (r,c) in visited):
                    return
            grid[r][c] = "0"
            visited.append((r,c))
            
            for x, y in dirs:
                dfs(r + x, c + y)

            

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1


        return res