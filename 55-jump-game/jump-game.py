class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = 1
        for n in nums:
            jumps -= 1
            if jumps < 0:
                return False
            if n > jumps:
                jumps = n
        return True