class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)

        return len(s) == 0