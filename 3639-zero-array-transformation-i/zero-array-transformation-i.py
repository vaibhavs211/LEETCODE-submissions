class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0]*(n+1)
        for query in queries:
            diff[query[0]] += 1
            diff[query[1] + 1] -= 1

        d = 0
        for i in range(n):
            d += diff[i]
            if nums[i]-d > 0:
                return False
        return True