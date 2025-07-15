class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1]*len(nums)
        s = []
        n = len(nums)
        for i in range(2*n):
            if s and s[-1][1]<nums[i%n]:
                while s and s[-1][1]<nums[i%n]:
                    res[s.pop()[0]] = nums[i%n]
            s.append([i%n,nums[i%n]])
        return res