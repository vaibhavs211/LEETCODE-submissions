class Solution:
    MOD = 10**9 + 7
    ways = [1,2,5]
    def numTilings(self, n: int) -> int:
        x = len(self.ways)
        if n<=x:
            return self.ways[n-1]
        else:
            for i in range(x,n):
                self.ways.append((2*self.ways[i-1] + self.ways[i-3]) % self.MOD)
            return self.ways[n-1]