class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = []
        pv_ct = 0
        for n in nums:
            if n < pivot:
                res.append(n)
            if n == pivot:
                pv_ct += 1
        res += [pivot] * pv_ct
        for n in nums:
            if n > pivot:
                res.append(n)
        return res