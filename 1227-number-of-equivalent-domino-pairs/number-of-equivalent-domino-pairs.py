from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = defaultdict(int)

        for dom in dominoes:
            if dom[0] > dom[1]:
                d[str(dom[1]) + str(dom[0])] += 1
            else:
                d[str(dom[0]) + str(dom[1])] += 1

        res = 0
        for key in d.keys():
            n = d[key]
            if n > 1:
                res += n*(n-1)//2
        return res