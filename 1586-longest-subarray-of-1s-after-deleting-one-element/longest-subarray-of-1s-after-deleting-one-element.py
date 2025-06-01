class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        zc = 0 
        oc = 0
        i = 0
        j = 0
        mx = 0
        if nums.count(0) == 0:
            return n-1
        while i<=j and j<n:
            while j<n and zc <= 1:
                if nums[j] == 1:
                    oc += 1
                else:
                    zc += 1
                j+=1
            mx = max(mx,oc)
            while i<j and zc>1:
                if nums[i] == 1:
                    oc -=1
                else:
                    zc -= 1
                i+=1
        return mx