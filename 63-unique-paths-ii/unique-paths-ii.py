from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @lru_cache(None)
        def helper(i,j,m,n):
            if i==m or j==n or obstacleGrid[i][j]:
                return 0
            if i == m-1 and j == n-1:
                return 1
            return helper(i+1,j,m,n) + helper(i,j+1,m,n)
        
        return helper(0,0,len(obstacleGrid),len(obstacleGrid[0]))