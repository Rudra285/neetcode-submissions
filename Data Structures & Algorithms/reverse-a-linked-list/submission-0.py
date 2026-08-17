# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        curr = head
        prev = None
        future = head.next
        while curr.next != None:
            if prev != None:
                curr.next = prev
            prev = curr
            curr = future
            future = curr.next
        head.next = None
        curr.next = prev
        return curr