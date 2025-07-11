# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left,right):
            head = None
            t = None
            while left and right:
                if left.val<right.val:
                    if not head:
                        head = left
                        t = head
                    else:
                        head.next = left
                        head = left
                    left = left.next
                else:
                    if not head:
                        head = right
                        t = head
                    else:
                        head.next = right
                        head = right
                    right = right.next
            if left:
                head.next = left
            if right:
                head.next = right
            return t
        
        def mergeSort(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            mid = slow.next
            slow.next = None
            head = mergeSort(head)
            mid = mergeSort(mid)
            return merge(head,mid)
        
        return mergeSort(head)