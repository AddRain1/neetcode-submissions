class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        minutes = 0
        fresh = 0

        def bfs(x, y):
            nonlocal fresh
            if (min(x,y) < 0 or x == rows or y == cols or grid[x][y] != 1):
                return
            q.append((x, y))
            grid[x][y] = 2
            fresh -= 1

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    q.append((x, y))
                if grid[x][y] == 1:
                    fresh += 1

        while q and fresh > 0:
            for i in range(len(q)):
                x, y = q.popleft()
                bfs(x + 1, y)
                bfs(x-1, y)
                bfs(x, y+1)
                bfs(x, y-1)
            minutes += 1

        return minutes if fresh == 0 else -1
                