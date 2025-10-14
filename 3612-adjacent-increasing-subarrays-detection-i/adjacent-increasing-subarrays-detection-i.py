class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        cur = 1
        if k == 1:
            return True
        for i in range(1,len(nums) - k):
            if nums[i] > nums[i-1] and nums[i+k] > nums[i+k-1]:
                cur += 1
                if cur == k:
                    return True
            else:
                cur = 1
        return False