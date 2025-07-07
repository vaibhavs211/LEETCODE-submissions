class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i<len(nums):
            if k and nums[i] < 0:
                nums[i] = 0-nums[i]
                k -= 1
                i += 1
            elif not k:
                return sum(nums)
            else:
                if k%2 == 0:
                    return sum(nums)
                else:
                    return sum(nums) - 2*(min(nums[i],nums[i-1]) if i!=0 else nums[i])
        if not k:
            return sum(nums)
        return sum(nums) - 2*nums[-1]