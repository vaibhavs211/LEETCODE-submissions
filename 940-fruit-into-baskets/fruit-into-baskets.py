from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        c = 0
        mx = 0
        n = len(fruits)
        i = 0
        for j in range(n):
            d[fruits[j]] += 1
            c += 1
            if len(d) > 2:
                while i<j and len(d) > 2:
                    d[fruits[i]] -= 1
                    c -= 1
                    if d[fruits[i]] == 0:
                        del d[fruits[i]]
                    i += 1
            if c > mx:
                mx = c
        return mx