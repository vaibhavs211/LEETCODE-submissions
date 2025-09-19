class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7
        return pow(20,n//2,MOD) if n%2 == 0 else (pow(5,n//2 + 1, MOD)*pow(4,n//2,MOD))%MOD