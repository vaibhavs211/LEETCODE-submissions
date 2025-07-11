from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = sorted(list(Counter(s).items()),key=lambda x:x[1], reverse=True)
        res =""
        for i,j in c:
            res += i*j
        return res
        