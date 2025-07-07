from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = Counter(nums)
        for i in range(len(nums)):
            if d[0]:
                nums[i] = 0
                d[0] -= 1
            elif d[1]:
                nums[i] = 1
                d[1] -= 1
            else:
                nums[i] = 2