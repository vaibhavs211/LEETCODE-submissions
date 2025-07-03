class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if l == r or (nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]):
                return nums[mid]
            
            if mid%2 == 0:
                if nums[mid-1] == nums[mid]:
                    r = mid - 2
                else:
                    l = mid + 2
            else:
                if nums[mid-1] == nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
