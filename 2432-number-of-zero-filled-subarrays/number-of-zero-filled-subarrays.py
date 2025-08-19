class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        tot = 0
        con = 0
        for el in nums:
            if el == 0:
                tot+=1
                con+=1
                if con>1:
                    tot+=con-1
            else:
                con = 0
        return tot