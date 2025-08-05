from functools import lru_cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def helper(i,j,m,n):
            if i==m or j==n:
                return float('inf')
            if i == m-1 and j == n-1:
                return grid[i][j]
            return min(helper(i+1,j,m,n), helper(i,j+1,m,n)) + grid[i][j]
        
        return helper(0,0,len(grid),len(grid[0]))