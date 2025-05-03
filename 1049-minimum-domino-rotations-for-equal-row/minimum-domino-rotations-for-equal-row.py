import statistics as stats
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t = stats.mode(tops)
        b = stats.mode(bottoms)

        c1 = tops.count(t)
        c2 = bottoms.count(b)

        n = len(tops)
        res = 0
        if c1>c2:
            for i in range(n):
                if tops[i] != t and bottoms[i] == t:
                    res += 1
                elif tops[i] != t:
                    return -1
        else:
            for i in range(n):
                if bottoms[i] != b and tops[i] == b:
                    res += 1
                elif bottoms[i] != b:
                    return -1

        return res