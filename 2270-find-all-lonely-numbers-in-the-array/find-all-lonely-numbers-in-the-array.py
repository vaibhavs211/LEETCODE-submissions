class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1
        res = []
        for x in d.keys():
            if d[x] == 1 and (x-1 not in d) and (x+1 not in d):
                res.append(x)
        return res
        