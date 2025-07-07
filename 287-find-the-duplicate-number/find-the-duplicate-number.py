class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        for i in nums:
            if visited[i]:
                return i
            visited[i]=True