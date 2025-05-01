class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm = sum(nums[:k])
        mx_sm = sm
        for i in range(k,len(nums)):
            sm += nums[i] - nums[i-k]
            if sm > mx_sm:
                mx_sm = sm
        return mx_sm/k