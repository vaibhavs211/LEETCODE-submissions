class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ns = nums.copy()
        n = len(nums)
        for i in range(n):
            nums[(i+k)%n] = ns[i]