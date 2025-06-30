from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = defaultdict(int)
        ps[0] = 1
        curr = 0
        res = 0
        for num in nums:
            curr = curr+num
            if (curr-k) in ps:
                res += ps[curr-k]
            ps[curr] += 1
        return res