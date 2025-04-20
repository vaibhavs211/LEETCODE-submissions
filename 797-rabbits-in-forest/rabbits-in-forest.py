class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = {}
        for n in answers:
            d[n] = d.get(n, 0) + 1

        res = 0
        for k in d.keys():
            if d[k] <= k+1:
                res += k+1
            else:
                res += math.ceil(d[k]/(k+1)) * (k + 1)

        return res