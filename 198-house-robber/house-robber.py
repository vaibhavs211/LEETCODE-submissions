from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        mx = 0
        @lru_cache(None)
        def helper(i,res):
            nonlocal mx
            if i >= len(nums):
                mx = max(mx,res)
                return 
            helper(i+2,res+nums[i])
            helper(i+1,res)
        helper(0,0)
        return mx