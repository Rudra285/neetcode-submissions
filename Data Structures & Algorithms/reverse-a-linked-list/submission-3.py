# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev2 = head
        if not head.next:
            return head
        prev = head.next

        if not prev.next:
            prev2.next = None
            prev.next = prev2
            return prev
        curr = head.next.next
        prev2.next = None
        while curr:
            prev.next = prev2
            prev2 = prev
            prev = curr
            curr = curr.next
        prev.next = prev2
        return prev
        