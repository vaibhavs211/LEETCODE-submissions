class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d = {}
        for i in range(value):
            d.update({i:0})
        for n in nums:
            d[n%value] += 1

        k = sorted(d.items(), key = lambda x:(x[1],x[0]))[0][0]
        return value*d[k]+k