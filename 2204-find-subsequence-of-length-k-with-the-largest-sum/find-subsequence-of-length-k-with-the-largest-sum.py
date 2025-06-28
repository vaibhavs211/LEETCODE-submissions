class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        new = [(nums[i],i) for i in range(n)]

        new = sorted(new, key = lambda x:x[0], reverse = True)
        new = new[:k]
        new.sort(key = lambda x:x[1])

        return [x[0] for x in new]