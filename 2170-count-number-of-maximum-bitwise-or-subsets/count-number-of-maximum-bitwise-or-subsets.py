class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for n in nums:
            mx|=n
        
        c = 0

        def helper(idx, res):
            nonlocal mx,c
            if idx == len(nums):
                if res == mx:
                    c += 1
                return 
            
            helper(idx + 1, res)
            helper(idx + 1, res | nums[idx])
        
        helper(0, 0)
        return c