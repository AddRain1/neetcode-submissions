class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def bfs(grid, x, y):
            if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
                return
            if grid[x][y] == '1':
                grid[x][y] = '0'
                bfs(grid, x + 1, y)
                bfs(grid, x - 1, y)
                bfs(grid, x, y + 1)
                bfs(grid, x, y - 1)
            
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    res += 1
                    bfs(grid, x, y)

        return res