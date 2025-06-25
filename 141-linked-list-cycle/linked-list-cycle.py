# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        temp1 = head
        temp2 = head.next
        while(temp1 and temp2):
            if temp1 == temp2:
                return True
            temp1 = temp1.next
            if temp2.next:
                temp2 = temp2.next.next
            else:
                return False
        return False