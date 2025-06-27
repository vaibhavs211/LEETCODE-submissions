class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)
        n = len(nums)
        for i in range(n):
            if target-nums[i] in s:
                for j in range(i+1,n):
                    if target - nums[i] == nums[j]:
                        return [i,j]
        