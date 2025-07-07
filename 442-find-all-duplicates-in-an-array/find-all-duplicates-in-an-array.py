class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1
            else:
                dup.append(abs(num))
        
        return dup