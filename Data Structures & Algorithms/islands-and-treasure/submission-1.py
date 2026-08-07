from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # go through each cell and find treasure
        # from each treasure, run bfs at the same time
        # if water or already has a number, then ignore

        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                new_dr = r + dr
                new_dc = c + dc

                if (new_dr < 0 or new_dr >= rows or new_dc < 0 or
                    new_dc >= cols or grid[new_dr][new_dc] != 2147483647):
                        continue

                grid[new_dr][new_dc] = grid[r][c] + 1
                queue.append((new_dr, new_dc))

                    