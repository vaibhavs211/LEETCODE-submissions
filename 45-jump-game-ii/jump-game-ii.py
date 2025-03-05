class Solution:
    def jump(self, nums: List[int]) -> int:
        # jumps = 1
        cnt = 0
        n = len(nums)
        i = 0
        if n == 1:
            return 0
        while i < n:
            cnt += 1
            if i + nums[i] >= n-1:
                return cnt
            t = nums[i]
            jp = -1000
            idx = -1
            for j in range(nums[i]):
                if i+j+1<n and (nums[i+j+1]-t+j) > jp:
                    jp = nums[i+j+1]-t+j
                    idx = i+j+1
            i = idx

        return cnt
