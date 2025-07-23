class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j = 0,0
        mn = float('inf')
        s = 0
        f = False
        while i<len(nums):
            while s<target and j<len(nums):
                s += nums[j]
                j+=1
            if s>= target and j-i < mn:
                f = True
                mn = j-i
            s -= nums[i]
            i += 1
        
        return mn if f else 0