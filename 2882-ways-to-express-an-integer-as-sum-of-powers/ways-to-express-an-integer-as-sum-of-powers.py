class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # dp = [[0]*(n+1) for _ in range(n+1)]
        # for i in range(1,n+1):
        #     for j in range(1,n+1):
        #         k = 1
        #         while k**x <= i:
        #             tot += dp[i-k**x][n+1]
        MOD = 10**9 + 7
        powers = []
        j = 1
        while j**x <= n:
            powers.append(j**x)
            j += 1
        
        dp = [0]*(n+1)
        dp[0] = 1
        for p in powers:
            for i in range(n,p-1,-1):
                dp[i] = (dp[i]+dp[i-p]) % MOD
        return dp[n]