# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_size = 0
        node = head
        
        while node:
            list_size += 1
            node = node.next
        
        remove_node = list_size - n
        if remove_node == 0:
            return head.next
        
        i = 0
        node = head
        for i in range(remove_node - 1):
            head = head.next
        head.next = head.next.next

        return node