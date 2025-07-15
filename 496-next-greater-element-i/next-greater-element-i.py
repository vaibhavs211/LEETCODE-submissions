class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        h = {}
        for n in nums2:
            if s and s[-1]<n:
                while s and s[-1]<n:
                    h.update({s.pop():n})
            s.append(n)
        
        for i,n in enumerate(nums1):
            nums1[i] = h[n] if n in h else -1
        return nums1
