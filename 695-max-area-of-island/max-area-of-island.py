class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            visited.add((i,j))
            count[0] += 1
            if i>0 and grid[i-1][j] and (i-1,j) not in visited:
                dfs(i-1,j)
            if i<size[0]-1 and grid[i+1][j] and (i+1,j) not in visited:
                dfs(i+1,j)
            if j>0 and grid[i][j-1] and (i,j-1) not in visited:
                dfs(i,j-1)
            if j<size[1]-1 and grid[i][j+1] and (i,j+1) not in visited:
                dfs(i,j+1)

            
        visited = set()
        count = [0]
        size = (len(grid), len(grid[0]))
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i,j) not in visited:
                    dfs(i,j)
                if count[0]>res:
                    res = count[0]
                count = [0]
        return res