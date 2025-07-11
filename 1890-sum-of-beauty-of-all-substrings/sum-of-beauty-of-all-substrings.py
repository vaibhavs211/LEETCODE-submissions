from collections import defaultdict
class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            h = defaultdict(int)
            for j in range(i,len(s)):
                h[ord(s[j])-97] += 1
                val = h.values()
                res += max(val) - min(val)
        return res