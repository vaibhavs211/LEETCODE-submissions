class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        subp = 1
        cur_mn = nums[0]
        for n in nums:
            if n - cur_mn > k:
                subp += 1
                cur_mn = n
        return subp