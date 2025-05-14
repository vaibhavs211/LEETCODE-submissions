class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j = 0,0
        z = 0
        n = len(nums)
        mx = 0
        for j in range(n):
            if nums[j] == 0:
                z += 1
            while z > k:
                if nums[i] == 0:
                    z -= 1
                i+=1
            mx = max(mx,j-i+1)
        return mx