class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set(nums)
        if max(s) == 0:
            return 0
        res = 0
        for n in sorted(list(s),reverse = True):
            if res and n<0:
                return res
            res += n
        return res