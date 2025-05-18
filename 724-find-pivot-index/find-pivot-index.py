class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        sm = 0
        for i in range(len(nums)):
            if i != 0:
                sm += nums[i-1]
            if sm == tot-sm-nums[i]:
                return i
        return -1