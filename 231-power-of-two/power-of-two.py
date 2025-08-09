# import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        tmp=n
        cnt = 0
        while(tmp>1):
            tmp = tmp>>1
            cnt+=1
        if n == 1<<cnt:
            return True
        else:
            return False