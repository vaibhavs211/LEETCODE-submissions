class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        l = []
        l.append(list(nums1-nums2))
        l.append(list(nums2-nums1))
        return l