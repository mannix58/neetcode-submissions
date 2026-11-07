class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = {}
        def dfs(r, c):
            if (r, c) in visited or not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != "1":
                return
            visited[(r,c)] = True
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) in visited:
                    continue
                if grid[r][c] == "0": continue
                dfs(r, c)
                islands += 1

        return islands