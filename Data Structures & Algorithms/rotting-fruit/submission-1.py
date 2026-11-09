from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque() 
        time = 0
        fresh = 0
        R,C = len(grid), len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r,c])

        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for d in DIRECTIONS:
                    x, y = curr[0] + d[0], curr[1] + d[1]
                    if x < 0 or y < 0 or x >= R or y >= C :
                        continue
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.append([x,y])
                        fresh -= 1
            time += 1

        return -1 if fresh > 0 else time

