from statistics import mode
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dom = mode(nums)
        i = 0
        cnt = nums.count(dom)
        c = 0
        n = len(nums)
        while i < n:
            if nums[i] == dom:
                c+= 1
                if (i+1)//2 < c and (n-i-1)//2 < (cnt-c):
                    return i
            i+=1
        return -1