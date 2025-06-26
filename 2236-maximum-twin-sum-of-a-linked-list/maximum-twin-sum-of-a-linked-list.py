# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next.next
        while fast:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        mx = 0
        while head:
            mx = max(mx,head.val+prev.val)
            head = head.next
            prev = prev.next
        return mx